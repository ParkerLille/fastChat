import os
from fastapi import APIRouter, HTTPException

from application.utils.logs import get_logger

app = APIRouter()


@app.get("/api")
async def api():
    """
    测试接口
    :return:
    """
    return {"Hello": f'{os.environ.get("APP_NAME")}'}


@app.get('/exception')
async def exception(name: str) -> dict:
    """测试异常接口"""
    try:
        print(name)
    except Exception as e:
        logger = get_logger(os.environ.get('APP_NAME'))
        logger.error(f"发生错误：{e}")
        raise HTTPException(detail=f"{e}", status_code=500)
    return {}