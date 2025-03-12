# -*- coding: utf-8 -*-
# @Time : 2025/3/11 17:49
# @Author : Nean
# -*- coding: utf-8 -*-
# @Time : 2025/3/10 22:10
# @Author : Nean
import os
from fastapi import FastAPI
from dotenv import load_dotenv
from tortoise.contrib.fastapi import register_tortoise
from .apps.common.views import app as common_app
from .apps.users.views import app as users_app

from . import settings
from .utils import middleware, exceptions, redis_tools


def create_app() -> FastAPI:
    """工厂函数：创建App对象"""
    # 读取环境配置文件的信息，加载到环境变量
    load_dotenv()
    print("启动成功：", os.environ.get("APP_NAME"))

    app = FastAPI(
        title=os.environ.get('APP_NAME'),
        summary=os.environ.get('APP_SUMMARY'),
        description=os.environ.get('APP_DESCRIPTION'),
        version=os.environ.get('APP_VERSION'),
        # 注册全局异常处理函数
        exception_handlers={
            exceptions.HTTPException: exceptions.global_http_exception_handler,
            exceptions.RequestValidationError: exceptions.global_request_exception_handler,
        }
    )

    # 把tortoise-orm注册到App应用对象中
    register_tortoise(
        app,
        config=settings.TORTOISE_ORM,
        generate_schemas=False,  # 是否自动生成表结构[自动根据配置项中apps.models的路径自动识别模型]
        add_exception_handlers=True,  # 是否启用自动异常处理
    )

    # redis连接对象注册到App应用对象中
    redis_tools.register_redis(
        app,
        config=settings.REDIS,
    )

    # 注册各个分组应用中的视图接口代码到App应用对象中
    app.include_router(common_app)
    app.include_router(users_app, prefix='/users')

    # 注册中间件函数
    http_middleware = app.middleware('http')
    http_middleware(middleware.log_requests)

    return app
