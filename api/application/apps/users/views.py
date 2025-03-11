# -*- coding: utf-8 -*-
# @Time : 2025/3/11 17:50
# @Author : Nean
from fastapi import APIRouter, HTTPException, status, Request
from . import scheams, models
from application.utils import wechat_tools

app = APIRouter()


@app.post("/register", response_model=scheams.UserRegisterResponse)
async def register(user_info: scheams.UserRegisterRequest):
    """处理用户注册请求"""
    # 1.账号唯一性验证
    user = await models.User.filter(mobile=user_info.mobile).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="手机号已注册，不能重复注册！",
        )

    # todo 判断验证码是否正确

    # 2. 通过小程序提交的code授权码到微信官方获取当前微信用户的openid和session_key
    wechat_user = wechat_tools.get_wechat_info(user_info.code)

    # 验证微信是否重复注册多个账号
    user = await models.User.filter(openid=wechat_user["openid"]).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="当前微信已绑定其他账号，不能重复绑定！",
        )

    # 3. 添加用户数据
    user = await models.User.create(
        **dict(user_info),
        username=user_info.mobile,
        avatar=user_info.avatarUrl,
        nickname=user_info.nickName,
        sex=user_info.gender,
        openid=wechat_user["openid"]
    )

    # 4. 返回结构
    return {
        "id": user.id,
        "nickname": user.nickname,
        "avatar": user.avatar,
        "code": status.HTTP_200_OK,
        "err_msg": "用户注册成功",
        "status": "Success",
        "token": "asdasdasasdasdasdad",  # todo
    }


@app.get("/login")
async def login():
    return {"methods": "login"}
