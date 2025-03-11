<template>
	<view class="page-layout">
		<view class="page-body" id="x_chat">
			<view :key="index" v-for="(message, index) in messages">
				<view class="chat-item-body">
					<view class="chat-item-time">{{message.time}}</view>
					<view key="index" v-if="message.type == 'ai'" class="chat-item-layout chat-left">
						<view class="chat-inner-layout">
							<view class="chat-item-name">{{message.sender}}</view>
							<view class="chat-item-msg-layout">
								<image class="chat-item-photo" v-if="message.photoUrl" :src="message.photoUrl"
									mode="aspectFit"></image>
								<view class="chat-inner-msg-left" v-html="message.text"></view>
							</view>
						</view>
					</view>
				</view>
				<view :key="index" v-if="message.type == 'sender'" class="chat-item-layout chat-right">
					<view class="chat-inner-layout">
						<view class="chat-item-name-right">{{message.sender}}</view>
						<view class="chat-item-msg-layout">
							<view class="chat-inner-msg-right" v-html="message.text"></view>
							<image class="chat-item-photo" v-if="message.photoUrl" :src="message.photoUrl"
								mode="aspectFit"></image>
						</view>
					</view>
				</view>
			</view>
		</view>
		<view class="submit-layout">
			<input class="submit-input" placeholder="点击输入，开始聊天吧" v-model="userInput" />
			<view class="submit-submit" type="submit" size="mini" @click="sendMessage">发送</view>
		</view>
	</view>
</template>

<script setup>
	import {
		ref
	} from "vue";
	const userInput = ref("");
	const messages = ref([{
			type: 'sender',
			text: '你是谁？',
			time: '2024-05-03 14:13:22',
			photoUrl: 'https://pic1.zhimg.com/80/v2-0aca47cf23db7047d051f03297312d64_720w.webp',
		},
		{
			type: 'ai',
			text: '我是ChatGPT，一个由OpenAI开发的大型语言模型。我基于GPT-4架构构建，旨在通过自然语言处理技术帮助用户解决各种问题、回答问题、提供建议和进行对话。<br><br>我能够理解和生成文本，处理从简单问题到复杂任务的广泛请求，包括但不限于编写代码、创建内容、提供解释和建议、以及进行翻译。我的知识库截止到2023年10月，这意味着我能提供的信息和回答基于我在那之前的训练数据。<br><br>我不是一个真人，而是一个由人工智能驱动的程序，旨在通过文本形式与用户进行互动。我的目的是帮助用户找到他们需要的信息，解决问题，或者提供有价值的对话。',
			time: '2024-01-26 13:43:15',
			photoUrl: 'https://www.lulinux.com/d/file/bigpic/az/234906/xldp0zb1vlw.png',
		}
	])

	const pageScrollToBottom = () => {
		let that = this;
		wx.createSelectorQuery().select('#x_chat').boundingClientRect(function(rect) {
			let top = rect.height * messages.value.length;
			wx.pageScrollTo({
				scrollTop: top,
				duration: 100
			})
		}).exec()
	}
	pageScrollToBottom();

	const sendMessage = () => {
		// 跳转登陆页面
		uni.navigateTo({
			url: '/pages/login/login',
		})
		return;
		if (userInput.value.trim() === '') return;
		const userMessage = {
			type: 'sender',
			text: userInput.value,
			time: '2024-01-26 13:59:12',
			photoUrl: 'https://pic2.zhimg.com/80/v2-ab37ad93a61fc94135f1c67ea2412c55_720w.webp',
		};
		messages.value.push(userMessage);
		userInput.value = '';
		pageScrollToBottom();
	}
</script>

<style>
	.page-layout {
		width: 100%;
		height: 100%;
		box-sizing: border-box;
	}

	.page-body {
		width: 100%;
		display: flex;
		flex-direction: column;
		padding-bottom: 56px;
	}

	.chat-item-body {
		display: flex;
		flex-direction: column;
		margin-top: 20rpx;
	}

	.chat-item-time {
		width: 100vw;
		text-align: center;
		font-size: 28rpx;
		color: #ccc;
		border-radius: 10rpx;
		margin-top: 40rpx;
	}

	.chat-item-layout {
		display: block;
		max-width: 82%;
		margin: 1rpx 5rpx;
		box-sizing: border-box;
		padding: 0 1rpx;
	}

	.chat-right {
		float: right;
	}

	.chat-left {
		float: left;
	}

	.chat-inner-layout {
		display: flex;
		flex-direction: column;
	}

	.chat-item-photo {
		width: 70rpx;
		height: 70rpx;
		min-width: 70rpx;
		min-height: 70rpx;
		border-radius: 50%;
	}

	.chat-item-msg-layout {
		display: flex;
		flex-direction: row;
	}

	.chat-item-name {
		display: flex;
		flex-direction: row;
		align-items: center;
		font-size: 28rpx;
		color: #999;
		border-radius: 10rpx;
		margin: 5rpx 0 0 80rpx;
	}

	.chat-item-name-right {
		display: flex;
		flex-direction: row;
		align-items: center;
		font-size: 28rpx;
		color: #999;
		border-radius: 10rpx;
		margin: 5rpx 0 0 5rpx;
	}

	.chat-inner-msg-left {
		display: inline-block;
		flex-direction: row;
		align-items: center;
		color: #000;
		font-size: 30rpx;
		border-radius: 10rpx;
		background: #eee;
		padding: 15rpx 15rpx 15rpx 25rpx;
		margin-left: 12rpx;
	}

	.chat-inner-msg-right {
		display: inline-block;
		color: #000;
		font-size: 30rpx;
		border-radius: 10rpx;
		background: #87EE5F;
		padding: 15rpx 5rpx 15rpx 15rpx;
		margin-right: 12rpx;
	}

	.submit-layout {
		position: absolute;
		bottom: 0;
		width: 100%;
		background: #eee;
		flex-direction: row;
	}

	.submit-layout {
		width: 100%;
		position: fixed;
		bottom: 0;
		border-top: 1px solid #ddd;
		padding: 10rpx 0;
		display: flex;
		flex-direction: row;
		align-items: center;
	}

	.submit-input {
		flex: 1;
		background: #fff;
		margin: 5rpx 10rpx;
		border-radius: 5rpx;
		padding: 15rpx 20rpx;
		color: #333;
		font-size: 30rpx;
	}

	.submit-submit {
		background-color: rgb(66, 157, 250);
		color: #fff;
		font-weight: 700;
		font-size: 30rpx;
		border-radius: 10rpx;
		padding: 18rpx 30rpx;
		margin-right: 10rpx;
		text-align: center;
	}
</style>