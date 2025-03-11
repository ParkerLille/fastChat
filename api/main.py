# -*- coding: utf-8 -*-
# @Time : 2025/3/11 17:49
# @Author : Nean
import uvicorn, os

from application import create_app, FastAPI

app: FastAPI = create_app()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=os.environ.get('APP_HOST', '0.0.0.0'),
        port=int(os.environ.get('APP_PORT', 8000)),
        reload=bool(os.environ.get('APP_DEBUG'))
    )
