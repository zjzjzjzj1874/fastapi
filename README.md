# Python

This is a simple fastapi web frame


### 创建代码库
GitHub创建一个Python仓库,这里命名为`fastapi`

### 拉取代码
将自己的代码库克隆到本地开发环境.替换自己的仓库名
```sql
git clone git@github.com:zjzjzjzj1874/fastapi.git
```

### 创建服务

* 创建主函数
创建一个名为`main.py`的函数并写入一下内容:
```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

* 启动项目
运行以下命令启动:
```shell
uvicorn main:app --reload
```
* 查看根路由:`http://0.0.0.0:8000`,输出以下内容:
```html
{
    "Hello": "World"
}
```
* 查看交互式文档,访问:`http://0.0.0.0:8000/docs`
  ![访问预览](./static/fastapi-docs.png)

至此,我们已经成功创建了一个基于fastapi创建的python的web服务.