from fastapi import FastAPI
from pydantic import BaseModel
import mimetypes
import random

class Item(BaseModel):
    image_path: str


app = FastAPI()


@app.post("/")
async def post(item: Item):
    """概要

    POSTリクエスト

    Args:
        request.json['image_path'] (str): 画像パス

    Returns:

    Examples:

    Note:

    """

    ng_res: dict = {
        "success": False,
        "message": "Error:E50012",
        "estimated_data": {}
    }

    if img_path_what(item.image_path):
        print(item.image_path)

        _class: int = random.randint(1,10)
        confidence: float = random.uniform(0,1)

        ok_res: dict = {
            "success": True,
            "message": "success",
            "estimated_data": {
                "class": _class,
                "confidence": confidence
            }
        }

        return ok_res
    return ng_res



def img_path_what(image_path: str):
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
        imgtype: str = str(mimetypes.guess_type(image_path)[0])
        if "image" in imgtype:
            return True
        else:
            pass
    except:
        return False