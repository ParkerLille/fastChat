# -*- coding: utf-8 -*-
# @Time : 2025/3/11 17:50
# @Author : Nean
from tortoise import models, fields


class User(models.Model):
    # 字段列表
    id = fields.IntField(pk=True, description="主键")
    username = fields.CharField(max_length=255, unique=True, description="账号")
    nickname = fields.CharField(max_length=255, index=True, description="昵称")
    password = fields.CharField(max_length=255, description="密码")
    openid = fields.CharField(max_length=255, unique=True, description="OpenID")
    mobile = fields.CharField(max_length=15, index=True, description="手机")
    avatar = fields.CharField(max_length=500, null=True, description="头像")
    province = fields.CharField(max_length=255, null=True, description="省份")
    city = fields.CharField(max_length=255, null=True, description="城市")
    sex = fields.BooleanField(default=True, null=True, description="性别")
    created_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_time = fields.DatetimeField(auto_now=True, description="更新时间")
    deleted_time = fields.DatetimeField(null=True, description="删除时间")

    # 元数据
    class Meta:
        table = "user_info"
        description = "用户信息"

    def __repr__(self):
        return f"User (id={self.id}, username={self.username})"

    __str__ = __repr__
