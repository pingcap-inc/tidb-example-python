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


import MySQLdb

# If you don't have a TiDB cluster, just register here:
# https://tidbcloud.com/console/clusters/create-cluster
# And get a TiDB Cloud Serverless Tier in 1 min (no kidding, and it's free now)

connection = MySQLdb.connect(
    host="<host>",
    port=4000,
    user="<username>",
    password="<password>",
    database="test",
    ssl_mode="VERIFY_IDENTITY",
    ssl={
        # MacOS / Alpine: "/etc/ssl/cert.pem"
        # Debian / Ubuntu / Arch: "/etc/ssl/certs/ca-certificates.crt"
        # RedHat / Fedora / CentOS / Mageia: "/etc/pki/tls/certs/ca-bundle.crt"
        # OpenSUSE: "/etc/ssl/ca-bundle.pem"
        "ca": "/etc/ssl/cert.pem"
    }
)
with connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION();")
        m = cursor.fetchone()
        print(m[0])
