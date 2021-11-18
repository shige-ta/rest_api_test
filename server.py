from flask import Flask, jsonify, request
import mimetypes
import pymysql.cursors
import random

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=["GET", "POST"])
def post():
    """概要

    POSTリクエスト

    Args:
        request.json['image_path'] (str): 画像パス

    Returns:

    Examples:

    Note:

    """

    ng_res = {
    "success": False,
    "message": "Error:E50012",
    "estimated_data": {}
    }

    if request.method == "POST":
        image_path = request.json['image_path']
        if img_path_what(image_path):
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
    return jsonify(ng_res)

def img_path_what(image_path):
    """概要

    画像拡張子確認

    Args:
        image_path (str): postで受け取った画像パス

    Returns:
        bool: image_pathが画像の拡張子か判定

    Examples:

        >>> img_path_what("/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg")
        True

        >>> img_path_what("/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.j")
        False

    Note:

    """

    try:
        imgtype = mimetypes.guess_type(image_path)[0] 
        if "image" in imgtype:
            return True
    except:
        return False
        

if __name__ == '__main__':
    app.run()