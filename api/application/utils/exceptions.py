# -*- coding: utf-8 -*-
# @Time : 2025/3/11 14:45
# @Author : Nean
import os
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import status
from .logs import get_logger

logger = get_logger(os.environ.get('APP_NAME'))


def global_http_exception_handler(request, exc):
    """
    全局HTTP异常处理函数
    :param request: 本次发生异常时客户端请求对象
    :param exc: 异常发生时的执行上下文对象，即异常对象
    :return:
    """

    logger.error(f"发生异常：{exc.detail}")

    return JSONResponse({
        'code': exc.status_code,
        'err_msg': exc.detail,
        'status': 'Failed'
    })


def global_request_exception_handler(request, exc):
    """
    全局请求校验异常处理函数
    :param request:
    :param exc:
    :return:
    """

    return JSONResponse({
        'code': status.HTTP_400_BAD_REQUEST,
        'err_msg': exc.errors()[0],
        'status': 'Failed'
    })
