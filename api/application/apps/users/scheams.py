# -*- coding: utf-8 -*-
# @Time : 2025/3/11 17:50
# @Author : Nean
from pydantic import BaseModel, fields, model_validator
from application import settings
from application.utils import tools


class UserRegisterRequest(BaseModel):
    """注册接口的请求数据结构"""
    mobile: str = fields.Field(pattern='^1[3-9]\d{9}', description='手机号')
    password: str = fields.Field(min_length=6, max_length=16, description='密码')
    sms_code: str = fields.Field(max_length=settings.SMS['length'], description='短信验证码')
    avatarUrl: str = fields.Field(description='微信头像')
    nickName: str = fields.Field(description='微信昵称')
    gender: bool = fields.Field(description='性别')
    province: str = fields.Field(description='省份')
    city: str = fields.Field(description='城市')
    code: str = fields.Field(description='微信授权码[10分钟内有效]')

    @model_validator(mode='after')
    def model_validator(self):
        # 对密码进行哈希加密
        hashing = tools.Hashing()
        self.password = hashing.hash(self.password)

        return self


class BaseResponse(BaseModel):
    code: int = fields.Field(description='状态码')
    err_msg: str = fields.Field(description='响应结果提示')
    status: str = fields.Field(description='状态文本提示')


class UserRegisterResponse(BaseResponse):
    """注册接口的响应数据结构"""
    id: int = fields.Field(description='用户ID')
    avatar: str = fields.Field(description='用户头像')
    nickname: str = fields.Field(description='用户昵称')
    token: str = fields.Field(description='Token令牌')
