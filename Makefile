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

.PHONY: recreate-table

test:
    make peewee-test sqlalchemy-test sqlalchemy-test mysqlclient-test pymysql-test mysql-connect-python-test

# helper
recreate-table:
    mycli --host 127.0.0.1 --port 4000 -u root --no-warn < player_init.sql

# ORMs
peewee-test:
    make recreate-table
	python peewee_example.py

sqlalchemy-test:
    make recreate-table
	python sqlalchemy_example.py

# Drivers
mysqlclient-test:
    make recreate-table
	python mysqlclient_example.py

pymysql-test:
    make recreate-table
	python pymysql_example.py

mysql-connect-python-test:
    make recreate-table
	python mysql_connect_python_example.py

