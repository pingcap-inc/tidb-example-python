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
import os
from dotenv import load_dotenv

import MySQLdb
import mysql.connector
import playhouse.db_url
import peewee
import pymysql
from pymysql.cursors import DictCursor as PyMySQLDictCursor
import sqlalchemy

class Config:
    def __init__(self):
        load_dotenv()
        self.tidb_host = os.getenv("TIDB_HOST", "127.0.0.1")
        self.tidb_port = int(os.getenv("TIDB_PORT", "4000"))
        self.tidb_user = os.getenv("TIDB_USER", "root")
        self.tidb_password = os.getenv("TIDB_PASSWORD", "")
        self.tidb_db_name = os.getenv("TIDB_DB_NAME", "test")
        self.require_ssl = os.getenv("REQUIRE_SSL", "false").lower() == "true"
        self.ca_path = os.getenv("CA_PATH", "")

        if self.require_ssl == True and self.ca_path == "":
            raise Exception(
                "CA_PATH is required when using serverless.\nIf you don't know how to get it, please refer to https://docs.pingcap.com/tidbcloud/secure-connections-to-serverless-clusters#root-certificate-default-path")

def get_mysqlclient_connection(autocommit:bool=True) -> MySQLdb.Connection:
    config = Config()
    db_conf = {
        "host": config.tidb_host,
        "port": config.tidb_port,
        "user": config.tidb_user,
        "password": config.tidb_password,
        "database": config.tidb_db_name,
        "autocommit": autocommit
    }

    if config.require_ssl:
        db_conf["ssl_mode"] = "VERIFY_IDENTITY"
        db_conf["ssl"] = {"ca": config.ca_path}

    return MySQLdb.connect(**db_conf)


def get_mysql_connector_python_connection(autocommit:bool=True) -> mysql.connector.MySQLConnection:
    config = Config()
    db_conf = {
        "host": config.tidb_host,
        "port": config.tidb_port,
        "user": config.tidb_user,
        "password": config.tidb_password,
        "database": config.tidb_db_name,
        "autocommit": autocommit
    }

    if config.require_ssl:
        db_conf["ssl_verify_identity"] = True
        db_conf["ssl_ca"] = config.ca_path

    return mysql.connector.connect(**db_conf)


def get_pymysql_connection(autocommit: bool = False) -> pymysql.Connection:
    config = Config()
    db_conf = {
        "host": config.tidb_host,
        "port": config.tidb_port,
        "user": config.tidb_user,
        "password": config.tidb_password,
        "database": config.tidb_db_name,
        "autocommit": autocommit,
        "cursorclass": PyMySQLDictCursor,
    }

    if config.require_ssl:
        db_conf["ssl_verify_cert"] = True
        db_conf["ssl_verify_identity"] = True
        db_conf["ssl_ca"] = config.ca_path

    return pymysql.connect(**db_conf)


def get_peewee_db() -> peewee.MySQLDatabase:
    config = Config()
    url = f'mysql://{config.tidb_user}:{config.tidb_password}@{config.tidb_host}:{config.tidb_port}/{config.tidb_db_name}'
    if config.require_ssl:
        return playhouse.db_url.connect(url, ssl_verify_cert=True, ssl_ca=config.ca_path)
    else:
        return playhouse.db_url.connect(url)


def get_sqlalchemy_engine():
    config = Config()
    url = f'mysql://{config.tidb_user}:{config.tidb_password}@{config.tidb_host}:{config.tidb_port}/{config.tidb_db_name}'
    if config.require_ssl:
        return sqlalchemy.create_engine(url, connect_args={
            "ssl_mode": "VERIFY_IDENTITY",
            "ssl": { "ca": config.ca_path }
        })
    else:
        return sqlalchemy.create_engine(url)


def __recreate_table(connection) -> None:
    with connection.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS player;")
        cur.execute("CREATE TABLE player (`id` VARCHAR(36), `coins` INTEGER, `goods` INTEGER, PRIMARY KEY (`id`));")

def mysqlclient_recreate_table() -> None:
    __recreate_table(get_mysqlclient_connection(autocommit=True))


def mysql_connector_python_recreate_table() -> None:
    __recreate_table(get_mysql_connector_python_connection(autocommit=True))


def pymysql_recreate_table() -> None:
    __recreate_table(get_pymysql_connection(autocommit=True))

