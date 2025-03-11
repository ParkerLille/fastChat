"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  __name: "index",
  setup(__props) {
    const userInput = common_vendor.ref("");
    const messages = common_vendor.ref([
      {
        type: "sender",
        text: "你是谁？",
        time: "2024-05-03 14:13:22",
        photoUrl: "https://pic1.zhimg.com/80/v2-0aca47cf23db7047d051f03297312d64_720w.webp"
      },
      {
        type: "ai",
        text: "我是ChatGPT，一个由OpenAI开发的大型语言模型。我基于GPT-4架构构建，旨在通过自然语言处理技术帮助用户解决各种问题、回答问题、提供建议和进行对话。<br><br>我能够理解和生成文本，处理从简单问题到复杂任务的广泛请求，包括但不限于编写代码、创建内容、提供解释和建议、以及进行翻译。我的知识库截止到2023年10月，这意味着我能提供的信息和回答基于我在那之前的训练数据。<br><br>我不是一个真人，而是一个由人工智能驱动的程序，旨在通过文本形式与用户进行互动。我的目的是帮助用户找到他们需要的信息，解决问题，或者提供有价值的对话。",
        time: "2024-01-26 13:43:15",
        photoUrl: "https://www.lulinux.com/d/file/bigpic/az/234906/xldp0zb1vlw.png"
      }
    ]);
    const pageScrollToBottom = () => {
      common_vendor.wx$1.createSelectorQuery().select("#x_chat").boundingClientRect(function(rect) {
        let top = rect.height * messages.value.length;
        common_vendor.wx$1.pageScrollTo({
          scrollTop: top,
          duration: 100
        });
      }).exec();
    };
    pageScrollToBottom();
    const sendMessage = () => {
      common_vendor.index.navigateTo({
        url: "/pages/login/login"
      });
      return;
    };
    return (_ctx, _cache) => {
      return {
        a: common_vendor.f(messages.value, (message, index, i0) => {
          return common_vendor.e({
            a: common_vendor.t(message.time),
            b: message.type == "ai"
          }, message.type == "ai" ? common_vendor.e({
            c: common_vendor.t(message.sender),
            d: message.photoUrl
          }, message.photoUrl ? {
            e: message.photoUrl
          } : {}, {
            f: message.text
          }) : {}, {
            g: message.type == "sender"
          }, message.type == "sender" ? common_vendor.e({
            h: common_vendor.t(message.sender),
            i: message.text,
            j: message.photoUrl
          }, message.photoUrl ? {
            k: message.photoUrl
          } : {}, {
            l: index
          }) : {}, {
            m: index
          });
        }),
        b: userInput.value,
        c: common_vendor.o(($event) => userInput.value = $event.detail.value),
        d: common_vendor.o(sendMessage)
      };
    };
  }
};
wx.createPage(_sfc_main);
//# sourceMappingURL=../../../.sourcemap/mp-weixin/pages/index/index.js.map
