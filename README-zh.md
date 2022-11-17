# tidb-example-python

[English](/README.md) | 中文

**tidb-example-python** 是 PingCAP 为 Python 连接 [TiDB](https://docs.pingcap.com/tidb/stable) 而编写的示例项目。你可以在这里找到以下示例：

**Driver**

- [PyMySQL](/pymysql_example.py) 示例
- [mysqlclient](/mysqlclient_example.py) 示例
- [mysql-connect-python](/mysql_connect_python_example.py) 示例

**ORM**

- [SQLAlchemy](/sqlalchemy_example.py) 示例
- [peewee](/peewee_example.py) 示例

**Framework**

- [Django](/django_example) 示例

**Scenario**

- [Serverless Tier 连接](/serverless_tier_example.py)示例
- [批量删除场景](/batch_delete.py)示例
- [批量更新场景](/batch_update.py)示例
- [避免写偏斜](/write_skew_example.py)示例
- [乐观/悲观事务](/txn_example.py)示例

## 依赖

- [TiDB](https://docs.pingcap.com/tidb/stable)
- [mycli](https://www.mycli.net/)
- [Python 3.6+](https://www.python.org/)

## 运行

### 整体运行 ORM / Driver 测试

```bash
make test
```

### 单独运行某项测试

以 `peewee_example.py` 为例：

1. 安装依赖：

    ```bash
    pip install -r requirement.txt
    ```

2. 初始化表

    ```bash
    mycli --host 127.0.0.1 --port 4000 -u root --no-warn < player_init.sql
    ```

3. 运行脚本

    ```bash
    python3 peewee_example.py
    ```