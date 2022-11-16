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
from threading import Thread, Semaphore

import MySQLdb


def create_connection(autocommit=True):
    return MySQLdb.connect(
        host="127.0.0.1",
        port=4000,
        user="root",
        password="",
        database="test",
        autocommit=autocommit
    )


def prepare_data():
    connection = create_connection(autocommit=True)
    with connection:
        with connection.cursor() as cursor:
            # create table
            cursor.execute("DROP TABLE IF EXISTS `doctors`")
            cursor.execute("CREATE TABLE `doctors` (" +
                           "    `id` int(11) NOT NULL," +
                           "    `name` varchar(255) DEFAULT NULL," +
                           "    `on_call` tinyint(1) DEFAULT NULL," +
                           "    `shift_id` int(11) DEFAULT NULL," +
                           "    PRIMARY KEY (`id`)," +
                           "    KEY `idx_shift_id` (`shift_id`)" +
                           ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin")

            # add data
            cursor.executemany("INSERT INTO `doctors` (`id`, `name`, `on_call`, `shift_id`) VALUES (%s, %s, %s, %s)",
                               [(1, "Alice", True, 123), (2, "Bob", True, 123), (3, "Carol", False, 123)])


def ask_for_leave(thread_id: int, txn1_run: Semaphore, doctor_id: int):
    connection = create_connection(False)
    txn_log_header = f"/* txn {thread_id} */"
    if thread_id != 1:
        txn_log_header = "\t" + txn_log_header

    with connection:
        with connection.cursor() as cursor:
            cursor.execute("BEGIN PESSIMISTIC")
            print(f'{txn_log_header} BEGIN PESSIMISTIC')

            try:
                # txn 1 should be waiting until txn 2 is done.
                if thread_id is 1:
                    txn1_run.acquire()

                current_on_call = "SELECT COUNT(*) AS `count` FROM `doctors` " \
                                  "WHERE `on_call` = %s AND `shift_id` = %s FOR UPDATE"
                cursor.execute(current_on_call, (True, 123))
                print(f'{txn_log_header} {current_on_call} successful')

                (count,) = cursor.fetchone()
                if count >= 2:
                    # if current on-call doctor has 2 or more, this doctor can leave
                    shift = "UPDATE `doctors` SET `on_call` = %s WHERE `id` = %s AND `shift_id` = %s"
                    cursor.execute(shift, (False, doctor_id, 123))
                    print(f'{txn_log_header} {shift} successful')
                else:
                    raise Exception("at least one doctor is on call")
            except Exception as err:
                connection.rollback()
                print(f'something went wrong: {err}')
            else:
                connection.commit()
            finally:
                # txn 2 is done. let txn 1 run again.
                if thread_id is 2:
                    txn1_run.release()


prepare_data()
semaphore = Semaphore(0)

docker1_ask_for_leave = Thread(target=ask_for_leave, kwargs={"thread_id": 1, "txn1_run": semaphore, "doctor_id": 1})
docker2_ask_for_leave = Thread(target=ask_for_leave, kwargs={"thread_id": 2, "txn1_run": semaphore, "doctor_id": 2})

docker1_ask_for_leave.start()
docker2_ask_for_leave.start()
docker1_ask_for_leave.join(timeout=10)
docker2_ask_for_leave.join(timeout=10)

