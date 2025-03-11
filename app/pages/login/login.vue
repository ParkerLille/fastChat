<template>
	<view class="content">
		<view class="loginBox">
			<h3 style="text-align: center;margin-bottom:120rpx;">欢迎登录</h3>
			<view class="inputBox">
				<view class="ipt">
					<uni-icons type="contact" size="24" color="rgb(66,157,250)"></uni-icons>
					<input type="text" value="" placeholder="请输入账号" />
				</view>
				<view class="ipt">
					<uni-icons type="eye" size="24" color="rgb(66,157,250)"></uni-icons>
					<input type="passsword" value="" placeholder="请输入密码" />
				</view>
				<view class="ipt">
					<uni-icons type="checkmarkempty" size="24" color="rgb(66,157,250)"></uni-icons>
					<input type="text" value="" placeholder="请输入验证码" />
					<view class="yzm">验证码</view>
				</view>
				<button class="login-btn">登录</button>
			</view>
			<view class="tipbox">
				<view class="txt"> —— 其他账号登录 —— </view>
				<view class="otherUser">
					<button>
						<uni-icons type="qq" size="40" color="rgb(66,157,250)"></uni-icons>
					</button>
					<button open-type="getUserInfo" @getuserinfo="wxLogin">
						<uni-icons type="weixin" size="40" color="rgb(2,187,17)"></uni-icons>
					</button>
				</view>
			</view>
		</view>
	</view>
</template>

<script setup>

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
		margin-top: 100rpx;
	}

	.otherUser {
		margin-top: 30rpx;
		display: flex;
		justify-content: center;
	}

	.otherUser button {
		margin: 0 10px;
		padding: 0;
		height: 42px;
		line-height: 42px;
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
	}
</style>