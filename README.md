# tidb-example-python

[![CI Workflow](https://github.com/pingcap-inc/tidb-example-python/actions/workflows/ci.yml/badge.svg)](https://github.com/pingcap-inc/tidb-example-python/actions/workflows/ci.yml)

English | [中文](/README-zh.md)

**tidb-example-python** is a sample project written by PingCAP for Python to connect to [TiDB](https://docs.pingcap.com/tidb/stable). You can find the following examples here.

## Driver

- [PyMySQL](/pymysql_example.py) example
- [mysqlclient](/mysqlclient_example.py) example
- [mysql-connector-python](/mysql_connector_python_example.py) example

## ORM

- [SQLAlchemy](/sqlalchemy_example.py) example
- [peewee](/peewee_example.py) example

## Framework

- [Django](/django_example) example

## Scenario

- [Serverless Tier connection](/serverless_tier_example.py) example
- [Butch delete](/batch_delete.py) example
- [Butch update](/batch_update.py) example
- [Avoid write skew](/write_skew_example.py) example
- [Optimistic and pessimistic transaction](/txn_example.py) example

## Prerequisites

- Python installed (recommended version 3.10 and above).
- Start your TiDB cluster. If you don't have a TiDB cluster yet:

  - We recommend referring to the document [Create a TiDB Serverless Cluster](https://docs.pingcap.com/tidb/stable/dev-guide-build-cluster-in-cloud) to create your own TiDB Cloud cluster.
  - Alternatively, you can refer to the documents [Deploy a Local Testing TiDB Cluster](https://docs.pingcap.com/tidb/stable/quick-start-with-tidb) or [Deploy a Formal TiDB Cluster](https://docs.pingcap.com/tidb/stable/production-deployment-using-tiup) to create a local cluster.

- Get the code and install the dependencies

  ```bash
  git clone https://github.com/pingcap-inc/tidb-example-python.git
  cd tidb-example-python
  pip install -r requirement.txt
  ```

- Configure the `.env` file in the code directory correctly. You can use `cp .env.example .env` to copy the initial configuration file and make changes accordingly. If you are unsure how to obtain this information, please refer to the documents [Obtain the connection parameters](https://docs.pingcap.com/tidbcloud/connect-via-standard-connection-serverless#obtain-the-connection-parameters) and [Where is the CA root path on my system?](https://docs.pingcap.com/tidbcloud/secure-connections-to-serverless-tier-clusters#where-is-the-ca-root-path-on-my-system):

  ```properties
  # TiDB cluster address
  TIDB_HOST='xxxxxxxx.aws.tidbcloud.com'
  # TiDB cluster port
  TIDB_PORT='4000'
  # TiDB cluster username
  TIDB_USER='xxxxxxxxxxx.root'
  # TiDB cluster password
  TIDB_PASSWORD='xxxxxxx'
  # The database name to be used for this example
  TIDB_DB_NAME='test'
  # Whether the used TiDB cluster is Serverless
  IS_SERVERLESS='true'
  # The location of the CA certificate on the instance where the example is run. Required when IS_SERVERLESS='true'
  CA_PATH='/etc/ssl/cert.pem'
  ```

## Run

### Run the Entire ORM / Driver Test

```bash
make test
```

### Run a specific test individually

Taking **peewee_example.py** as an example: `python3 peewee_example.py`.
