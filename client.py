import pymysql.cursors
import requests
import json
import datetime
import configparser

def db_insert(data):
    """概要

    db保存

    Args:
        data (dict): 保存するデータ

    Returns:

    Examples:
        >>> data = {'estimated_data': {'class': 8, 'confidence': 0.3808765467312175}, 'message': 'success', 'success': True, 'request_timestamp': '1637232849', 'response_timestamp': '1637232849', 'image_path': '/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg'}
        >>> db_insert(data)

    Note:

    """

    # 設定ファイル
    config = configparser.ConfigParser()
    config.read('db.ini')

    # MySQLに接続する
    connection = pymysql.connect(host=config['DEFAULT']['host'],
                                user=config['DEFAULT']['user'],
                                password=config['DEFAULT']['password'],
                                db=config['DEFAULT']['db'],
                                charset=config['DEFAULT']['charset'],
                                cursorclass=pymysql.cursors.DictCursor,
    )

    with connection.cursor() as cursor:
        c: list = ["%s" for i in range(len(data))]
        keys: list =  data.keys()
        values: list = [data[i] for i in keys]
        sql: str = "INSERT INTO ai_analysis_log ("+ ",".join(keys) + ") VALUES (" + ",".join(c) + ")"
        r = cursor.execute(sql, (values))
        print(r) # -> 1
        connection.commit()

    # MySQLから切断する
    connection.close()

if __name__ == '__main__':
    # リクエスト
    url: str = "http://localhost:5000/"
    image_path: str = "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"
    payload: str = json.dumps({"image_path": image_path})
    request_timestamp: datetime.datetime = datetime.datetime.now()
    res = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})
    
    # レスポンスをdbに保存
    response_timestamp: datetime.datetime = datetime.datetime.now()
    data:dict = json.loads(res.text)
    data_list: dict = {}
    try:
        data_list['confidence'] = data['estimated_data']['confidence']
        data_list['class'] = data['estimated_data']['class']
    except:
        pass
    data_list['success'] = data['success']
    data_list['request_timestamp'] = f'{int(request_timestamp.timestamp())}'
    data_list['response_timestamp'] = f'{int(response_timestamp.timestamp())}'
    data_list["image_path"] = image_path
    db_insert(data_list)