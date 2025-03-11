# -*- coding: utf-8 -*-
# @Time : 2025/3/11 12:42
# @Author : Nean
import os, time
from .logs import get_logger


async def log_requests(request, call_next):
    """日志中间件"""
    logger = get_logger(os.environ.get('APP_NAME'))
    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    logger.info(f"path={request.url.path} timer={formatted_process_time}ms status_code={response.status_code}")
    return response
