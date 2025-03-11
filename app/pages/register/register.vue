<template>
	<view class="content">
		<view class="loginBox">
			<h3 style="text-align: center;margin-bottom:120rpx;">欢迎注册</h3>
			<view class="inputBox">
				<view class="ipt">
					<uni-icons type="contact" size="24" color="rgb(66,157,250)"></uni-icons>
					<input type="text" v-model="user_info.mobile" placeholder="请输入手机号" />
				</view>
				<view class="ipt">
					<uni-icons type="eye" size="24" color="rgb(66,157,250)"></uni-icons>
					<input type="password" v-model="user_info.password" placeholder="请输入密码" />
				</view>
				<view class="ipt">
					<uni-icons type="checkmarkempty" size="24" color="rgb(66,157,250)"></uni-icons>
					<input type="text" v-model="user_info.sms_code" placeholder="请输入验证码" />
					<view class="yzm">验证码</view>
				</view>
				<button class="login-btn" open-type="getUserInfo" @getuserinfo="userRegister">注册</button>
			</view>
			<view class="txt reg-btn">
				<navigator url="/pages/login/login" hover-class="navigator-hover">已有账号？点击登陆 </navigator>
			</view>
		</view>
	</view>
</template>

<script setup>
	import {
		ref,
		reactive
	} from 'vue';

	// 用户注册信息
	const user_info = reactive({
		mobile: "",
		password: "",
		sms_code: "",
	})

	const userRegister = (e) => {
		// 用户注册请求
		console.log(e);
		uni.login({
			provider: 'weixin',
			success(response) {
				console.log(response.code);
				// 发送用户的注册数据到fastAPI服务端
				uni.request({
					method: "POST",
					url: "http://127.0.0.1:8000/users/register",
					data: {
						code: response.code,
						...user_info,
						...e.detail.userInfo
					}
				})
			}
		})
	}
</script>

<style scoped>
	svg {
		position: absolute;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 40%;
		box-sizing: border-box;
		display: block;
		background-color: #ffffff;
	}

	.loginBox {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -60%);
		width: 90%;
		border-radius: 20rpx;
		padding: 60rpx;
		box-sizing: border-box;
	}

	h3 {
		color: rgb(66, 157, 250);
		font-size: 40rpx;
		letter-spacing: 10rpx;
		margin-bottom: 40rpx;
	}

	.inputBox {}

	.ipt {
		height: 86rpx;
		display: flex;
		justify-content: flex-start;
		align-items: center;
		margin-bottom: 40rpx;
		background-color: #f5f5f5;
		border-radius: 10rpx;
		padding-left: 10rpx;
	}

	.ipt input {
		margin-left: 20rpx;
		font-size: 28rpx;
	}

	.ipt input {
		margin-left: 20rpx;
		min-width: 340rpx;
	}

	.forgetPwd {
		margin-top: 30rpx;
		font-size: 26rpx;
		color: #b5b5b5;
		text-align: end;
		padding: 0 10rpx;
		display: flex;
		justify-content: space-between;
	}

	.login-btn {
		margin-top: 20rpx;
		line-height: 85rpx;
		text-align: center;
		background: rgb(66, 157, 250);
		border-radius: 40rpx;
		color: #fff;
		margin-top: 40rpx;
	}

	.tip {
		text-align: center;
		font-size: 28rpx;
		position: fixed;
		bottom: 50rpx;
		left: 50%;
		transform: translate(-50%, -50%);
		color: #f4f4f4;
	}

	.tipbox {
		text-align: center;
		margin-top: 50rpx;
	}

	.otherUser {
		margin-top: 30rpx;
		display: flex;
		justify-content: center;
	}

	.otherUser button {
		margin: 0 10px;
		padding: 0;
		height: 84rpx;
		width: 84rpx;
		line-height: 84rpx;
		background: transparent;
		border: 1px solid transparent;
		outline: none;
	}

	.txt {
		font-size: 28rpx;
		color: #cbcbcb;
	}

	.otherUser .uni-icons {
		margin-left: 20rpx;
	}

	.yzm {
		text-align: end;
		font-size: 24rpx;
		background: rgb(66, 157, 250);
		height: 60rpx;
		width: 150rpx;
		line-height: 60rpx;
		text-align: center;
		border-radius: 10rpx;
		color: #fff;
		margin-left: 20rpx;
	}

	.reg-btn {
		margin-top: 10px;
		text-align: right;
	}
</style>