# -*- coding: utf-8 -*-
# @Time : 2025/3/12 11:28
# @Author : Nean
from redis import asyncio as aioredis
from fastapi import FastAPI


def register_redis(app: FastAPI, config: dict):
    """
    注册Redis连接对象到App应用对象中
    :param app:
    :param config:
    :return:
    """

    async def redis_pool():
        redis = await aioredis.from_url(f"redis://{config['host']}:{config['port']}/{config['db']}",
                                        decode_responses=True)
        return redis

    @app.on_event("startup")
    async def startup_event():
        app.state.redis = await redis_pool()
