import pymysql.cursors
import requests
import json
import datetime

def db_insert(data):
    # MySQLに接続する
    connection = pymysql.connect(host='localhost',
                                user='shigeta',
                                password='abcd',
                                db='deepwork1',
                                charset='utf8',
                                # cursorclassを指定することで
                                # Select結果をtupleではなくdictionaryで受け取れる
                                cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        if data['message'] != 'Error:E50012':
            sql = "INSERT INTO ai_analysis_log (image_path,success,message,class,confidence,request_timestamp,response_timestamp) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            r = cursor.execute(sql, (data['image_path'],data['success'],data['message'],data['estimated_data']['class'],data['estimated_data']['confidence'],data['request_timestamp'],data['response_timestamp']))
        else:
            sql = "INSERT INTO ai_analysis_log (image_path,success,message,request_timestamp,response_timestamp) VALUES (%s,%s,%s,%s,%s)"
            r = cursor.execute(sql, (data['image_path'],data['success'],data['message'],data['request_timestamp'],data['response_timestamp']))

        print(r) # -> 1
        # autocommitではないので、明示的にコミットする
        connection.commit()

    # MySQLから切断する
    connection.close()

if __name__ == '__main__':
    url = "http://localhost:5000/"
    image_path = "/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg"
    payload = json.dumps({"image_path": image_path})
    request_timestamp = datetime.datetime.now()
    res = requests.post(url, data=payload, headers={'Content-Type': 'application/json'})
    
    response_timestamp = datetime.datetime.now()
    # print(res.content['']))
    data = res.text
    data = json.loads(data)

    data['request_timestamp'] = f'{int(request_timestamp.timestamp())}'
    data['response_timestamp'] = f'{int(response_timestamp.timestamp())}'
    data["image_path"] = image_path

    db_insert(data)