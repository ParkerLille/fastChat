# -*- coding: utf-8 -*-
# @Time : 2025/3/10 22:10
# @Author : Nean
import uvicorn
import os
from application import create_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=os.environ.get('APP_HOST', '0.0.0.0'),
        port=int(os.environ.get('APP_PORT', 8000)),
        reload=bool(os.environ.get('APP_DEBUG'))
    )
