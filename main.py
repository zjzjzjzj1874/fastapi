from typing import Union

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from pymongo import MongoClient

from model import model
from model.model import MediaRecord
from loguru import logger

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")  # mongo客户端
db = client["test"]


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None  # bool类型,默认None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None]):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/videos/")
async def create_video(video_id: str, video_url: str):
    video = {"video_id": video_id, "video_url": video_url}
    result = db["t_test"].insert_one(video)
    if result:
        return {"message": f"Video {video_id} inserted."}
    else:
        raise HTTPException(status_code=400, detail="Insert video failed.")


@app.post("/record/")
async def create_record(url: str, content_id: str):
    r = MediaRecord(url=url, state=1, content_type=1)
    record = r.dict()
    result = db["t_record"].insert_one(record)
    if result:
        return {"message": f"t_record {content_id} inserted."}
    else:
        raise HTTPException(status_code=400, detail="Insert t_record failed.")


@app.get("/videos/")
async def read_videos():
    videos = []
    for video in db["t_test"].find():
        video["_id"] = str(video["_id"])
        videos.append(video)
    return videos


@app.get("/records/")
async def read_records():
    records = []
    for record in db["t_record"].find():
        record["_id"] = str(record["_id"])
        records.append(record)
    return records


@app.post(
    "/callback",
    tags=["3rd_party"],
    response_model=model.RespContent,
)
def callback(
        contents: model.ReqContent,
        request: Request,
):

    logger.info(f"Receive:{contents}")
    result = {
        "code": 200,
    }
    return result


# 新增配置
class AddConfigRequest(BaseModel):
    name: str
    notice_type: int = Field(1, alias="noticeType")


@app.post("/test-post/")
async def test_post(request: Request, item: AddConfigRequest):
    print(item.dict())
    print("type ==== ", item.notice_type)

    return {"message": f"Name {item.name} inserted."}

