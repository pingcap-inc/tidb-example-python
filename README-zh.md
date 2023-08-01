# tidb-example-python

[![CI Workflow](https://github.com/pingcap-inc/tidb-example-python/actions/workflows/ci.yml/badge.svg)](https://github.com/pingcap-inc/tidb-example-python/actions/workflows/ci.yml)

[English](/README.md) | 中文

**tidb-example-python** 是 PingCAP 为 Python 连接 [TiDB](https://docs.pingcap.com/tidb/stable) 而编写的示例项目。你可以在这里找到以下示例：

## Driver

- [PyMySQL](/pymysql_example.py) 示例
- [mysqlclient](/mysqlclient_example.py) 示例
- [mysql-connector-python](/mysql_connector_python_example.py) 示例

## ORM

- [SQLAlchemy](/sqlalchemy_example.py) 示例
- [peewee](/peewee_example.py) 示例

## Framework

- [Django](/django_example) 示例

## Scenario

- [Serverless Tier 连接](/serverless_tier_example.py)示例
- [批量删除场景](/batch_delete.py)示例
- [批量更新场景](/batch_update.py)示例
- [避免写偏斜](/write_skew_example.py)示例
- [乐观/悲观事务](/txn_example.py)示例

## 前提要求

- 已安装 [Python](https://www.python.org/)，推荐版本 3.10 及以上。
- 启动你的 TiDB 集群，如果你还没有 TiDB 集群：

  - 推荐参考[创建 TiDB Serverless 集群](https://docs.pingcap.com/zh/tidb/stable/dev-guide-build-cluster-in-cloud)文档创建你自己的 TiDB Cloud 集群。
  - 备选参考[部署本地测试 TiDB 集群](https://docs.pingcap.com/zh/tidb/stable/quick-start-with-tidb)或[部署正式 TiDB 集群](https://docs.pingcap.com/zh/tidb/stable/production-deployment-using-tiup)文档创建本地集群。

- 已获取代码并安装依赖

    ```bash
    git clone https://github.com/pingcap-inc/tidb-example-python.git
    cd tidb-example-python
    pip install requirement.txt
    ```

- 已正确配置代码目录下的 `.env` 配置文件，你可以用 `cp .env.example .env` 复制初始配置文件后进行更改。如果你不知道这些信息如何获取，请参考 [Obtain the connection parameters](https://docs.pingcap.com/tidbcloud/connect-via-standard-connection-serverless#obtain-the-connection-parameters) 及 [Where is the CA root path on my system?](https://docs.pingcap.com/tidbcloud/secure-connections-to-serverless-tier-clusters#where-is-the-ca-root-path-on-my-system) 文档：

    ```properties
    # TiDB 集群地址
    TIDB_HOST='xxxxxxxx.aws.tidbcloud.com'
    # TiDB 集群端口
    TIDB_PORT='4000'
    # TiDB 集群用户名
    TIDB_USER='xxxxxxxxxxx.root'
    # TiDB 集群密码
    TIDB_PASSWORD='xxxxxxx'
    # 希望本示例使用的数据库名称
    TIDB_DB_NAME='test'
    # 使用的 TiDB 集群是否是 Serverless
    IS_SERVERLESS='true'
    # 运行示例的实例上，CA 证书存在的位置，在 IS_SERVERLESS='true' 时必需
    CA_PATH='/etc/ssl/cert.pem'
    ```

## 运行

### 整体运行 ORM / Driver 测试

```bash
make test
```

### 单独运行某项测试

以 **peewee_example.py** 为例：`python3 peewee_example.py`。
