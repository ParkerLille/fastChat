# -*- coding: utf-8 -*-
# @Time : 2025/3/11 17:50
# @Author : Nean
import os
from fastapi import APIRouter, HTTPException, Request
from alibabacloud_tea_openapi import models as open_api_models
from application import settings
from application.utils import tools, logs
from alibabacloud_dysmsapi20170525.client import Client as Client
from alibabacloud_dysmsapi20170525 import models as models
from Tea.exceptions import UnretryableException, TeaException

logger = logs.getLogger(os.environ.get('APP_NAME'))

app = APIRouter()


@app.get('/api')
async def api() -> dict:
    """
    测试api接口
    :return:
    """
    return {'title': 'fastchat test api'}


@app.get('/sms/{mobile}')
async def sms(request: Request, mobile: str) -> dict:
    """发送验证码"""
    redis = request.app.state.redis
    # 1. 生成指定长度随机验证码
    sms_code = tools.genint(settings.SMS['length'])
    # 2. 调用redis保存验证码和手机号
    ret = await redis.setex(f'sms_{mobile}', settings.SMS['expire'], sms_code)
    # 3. 发送验证码短信
    config = open_api_models.Config(
        # 您的AccessKey ID,
        access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
        # 您的AccessKey Secret,
        access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'],
        # 访问的域名
        endpoint="dysmsapi.aliyuncs.com"
    )
    client = Client(config)
    request = models.SendSmsRequest(
        phone_numbers=mobile,
        sign_name=settings.ALIYUN['sms']['sign_name'],
        template_code=settings.ALIYUN['sms']['template_code'],
        template_param='{"code": %s}' % sms_code,
    )
    try:
        response = client.send_sms(request)
        print(response.body)
    except UnretryableException as e:
        # 网络异常
        print(e)
    except TeaException as e:
        # 业务异常
        print(e)
    except Exception as e:
        # 其他异常
        print(e)
    return {
        'code': 200,
        'err_msg': '短信已发送，请留意手机',
        'status': 'Success',
    }
