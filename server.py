from flask import Flask, jsonify, request
import mimetypes
# モジュール読み込み
import pymysql.cursors
import random

app = Flask(__name__)

# 日本語を使えるように
app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=["GET", "POST"])
def post():

    ng_res = {
    "success": False,
    "message": "Error:E50012",
    "estimated_data": {}
    }

    if request.method == "POST":
        image_path = request.json['image_path']
        if img_path_what(image_path):
            db_insert(image_path)
            print(image_path)

            _class = random.randint(1,10)
            confidence = random.uniform(0,1)

            ok_res = {
                "success": True,
                "message": "success",
                "estimated_data": {
                "class": _class,
                "confidence": confidence
                }
            }

            return jsonify(ok_res)
        else:
            return jsonify(ng_res)
    else:
        return jsonify(ng_res)


def img_path_what(image_path):
    flg = False
    try:
        imgtype = mimetypes.guess_type(image_path)[0] 
        if "image" in imgtype:
            flg = True
    except:
        flg = False
    finally:
        return flg

def db_insert(image_path):
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
        sql = "INSERT INTO ai_analysis_log (image_path) VALUES (%s)"
        r = cursor.execute(sql, (image_path))
        print(r) # -> 1
        # autocommitではないので、明示的にコミットする
        connection.commit()

    # MySQLから切断する
    connection.close()

if __name__ == '__main__':
    app.run()