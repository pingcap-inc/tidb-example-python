# Expected-Output

## SQLAlchemy

```
Player(id='test', coins=1, goods=1)
number of players: 1920
Player(id='test', coins=1, goods=1)
Player(id='7bfb8366-c993-4067-b3b8-11ad592f2a4a', coins=10000, goods=10000)
Player(id='551c729a-814c-4bb3-a65a-3f57d9ac365f', coins=10000, goods=10000)
buy player 1 coins not enough
trade success
Player(id='1', coins=0, goods=2)
Player(id='2', coins=114614, goods=18)
```

## peewee

```
id:test, coins:1, goods:1
number of players: 1920
id:test, coins:1, goods:1
id:24403111-9b03-4a19-81b2-2ac04619c23b, coins:10000, goods:10000
id:4e858c2c-9431-4508-8833-ac260511477e, coins:10000, goods:10000
buy player 1 coins not enough
trade success
id:1, coins:0, goods:2
id:2, coins:114614, goods:18
```

## mysqlclient

```
id:test, coins:1, goods:1
number of players: 1920
id:test, coins:1, goods:1
id:3189a139-c2a9-4b38-9daf-ee8e8d673f46, coins:10000, goods:10000
id:d0be8d6e-ec32-40af-9fd5-deeda0979362, coins:10000, goods:10000
buy player 1 coins not enough
trade success
id:1, coins:0, goods:2
id:2, coins:114614, goods:18
```

## PyMySQL

```
{'id': 'test', 'coins': 1, 'goods': 1}
number of players: 1920
{'id': 'test', 'coins': 1, 'goods': 1}
{'id': '6b8228fa-6ce8-4d06-88e1-380f6a5b4cd7', 'coins': 10000, 'goods': 10000}
{'id': '3496dbb8-3bbf-4a0b-897d-9757b8bd9a37', 'coins': 10000, 'goods': 10000}
buy player 1 coins not enough
trade success
{'id': '1', 'coins': 0, 'goods': 2}
{'id': '2', 'coins': 114614, 'goods': 18}
```

## mysql-connector-python

```
id:test, coins:1, goods:1
number of players: 1920
id:test, coins:1, goods:1
id:13354a97-7eed-4897-a890-b69761adddef, coins:10000, goods:10000
id:d8c92088-c519-4be1-89c4-b36bd6a595a0, coins:10000, goods:10000
buy player 1 coins not enough
trade success
id:1, coins:0, goods:2
id:2, coins:114614, goods:18
```