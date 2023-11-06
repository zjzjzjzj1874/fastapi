from typing import List, Tuple, Union, Dict

from pydantic import BaseModel
from pymongo import MongoClient


# 数据库表格
from model.config import MONGO_URL


class MediaRecord(BaseModel):
    content_type: int  # 类型  3音频  4视频
    url: str  # 资源地址
    state: int   # 状态 1 待送审 2已送审待回调 3已回调


mongoClient = MongoClient(MONGO_URL)  # mongo客户端
fastapiDB = mongoClient["fastproxy"]  # mongo数据库
media_record = fastapiDB.get_collection("media_record")


class RespContent(BaseModel):
    code: int = 0
    lang: str = "zh_CN"
    msg: str = "成功"


class ExtraPass(BaseModel):
    passThrough: str


class RequestParams(BaseModel):
    extra: Union[ExtraPass, Dict] = {}


class ReqContent(BaseModel):
    code: int
    btId: str
    requestId: str
    requestParams: Union[RequestParams, Dict] = {}
