# -*- coding: utf-8 -*-
# @Time : 2025/3/11 17:50
# @Author : Nean
import os
from fastapi import APIRouter, HTTPException

from application.utils import tools, logs

logger = logs.getLogger(os.environ.get('APP_NAME'))

app = APIRouter()


@app.get('/api')
async def api() -> dict:
    """
    测试api接口
    :return:
    """
    return {'title': 'fastchat test api'}

