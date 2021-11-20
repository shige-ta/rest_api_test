# rest_api_test

mysql接続設定コンフィグ編集

db.ini
```ini
[DEFAULT]
host=localhost
user="ユーザー名"
password="パスワード"
db="データベース名"
charset=utf8
```

Mock起動
```bash
python3 server.py
```

本プログラム起動
```bash
python3 client.py
```

本プログラム起動(fastapi version)
```bash
python3 server_fastapi_ver.py
```

![server_fastapi_ver](https://github.com/shige-ta/rest_api_test/blob/main/server_fastapi_ver.png)
