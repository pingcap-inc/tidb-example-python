# Copyright 2022 PingCAP, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
from connect_tidb import get_mysqlclient_connection

def update_batch(cur, last_book_id: int = None, last_user_id: int = None) -> (int, int):
    if last_book_id is None or last_user_id is None:
        cur.execute("SELECT `book_id`, `user_id` FROM `bookshop`.`ratings` "
                    "WHERE `ten_point` != true "
                    "ORDER BY `book_id`, `user_id` LIMIT 1000")
    else:
        cur.execute("SELECT `book_id`, `user_id` FROM `bookshop`.`ratings` "
                    "WHERE `ten_point` != true AND `book_id` > %s AND `user_id` > %s "
                    "ORDER BY `book_id`, `user_id` LIMIT 1000", (last_book_id, last_user_id))

    id_list = cur.fetchall()
    param_list = []
    latest_book_id, latest_user_id = None, None
    for book_id, user_id in id_list:
        latest_book_id, latest_user_id = book_id, user_id
        param_list.append(latest_book_id)
        param_list.append(latest_user_id)

    place_holder = "(%s,%s)" + ",(%s,%s)" * (len(id_list) - 1)
    update_sql = "UPDATE `bookshop`.`ratings` SET `ten_point` = true, " \
                 f"`score` = `score` * 2 WHERE (`book_id`, `user_id`) IN ({place_holder})"
    cur.execute(update_sql, tuple(param_list))
    return latest_book_id, latest_user_id


with get_mysqlclient_connection() as connection:
    with connection.cursor() as cursor:
        # add a column `ten_point`
        # cursor.execute("ALTER TABLE `bookshop`.`ratings` ADD COLUMN `ten_point` BOOL NOT NULL DEFAULT FALSE")
        # select at most 1000 primary keys in five-point scale data
        current_book_id, current_user_id = update_batch(cursor)
        print("first time batch update success")
        while True:
            current_book_id, current_user_id = update_batch(cursor, current_book_id, current_user_id)
            print(f"batch update success,book_id: {current_book_id}, user_id: {current_user_id}")
            time.sleep(1)
