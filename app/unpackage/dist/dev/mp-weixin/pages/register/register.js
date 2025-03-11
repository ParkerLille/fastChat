"use strict";
const common_vendor = require("../../common/vendor.js");
if (!Array) {
  const _component_uni_icons = common_vendor.resolveComponent("uni-icons");
  _component_uni_icons();
}
const _sfc_main = {
  __name: "register",
  setup(__props) {
    const user_info = common_vendor.reactive({
      mobile: "",
      password: "",
      sms_code: ""
    });
    const userRegister = (e) => {
      common_vendor.index.__f__("log", "at pages/register/register.vue:43", e);
      common_vendor.index.login({
        provider: "weixin",
        success(response) {
          common_vendor.index.__f__("log", "at pages/register/register.vue:47", response.code);
          common_vendor.index.request({
            method: "POST",
            url: "http://127.0.0.1:8000/users/register",
            data: {
              code: response.code,
              ...user_info,
              ...e.detail.userInfo
            }
          });
        }
      });
    };
    return (_ctx, _cache) => {
      return {
        a: common_vendor.p({
          type: "contact",
          size: "24",
          color: "rgb(66,157,250)"
        }),
        b: user_info.mobile,
        c: common_vendor.o(($event) => user_info.mobile = $event.detail.value),
        d: common_vendor.p({
          type: "eye",
          size: "24",
          color: "rgb(66,157,250)"
        }),
        e: user_info.password,
        f: common_vendor.o(($event) => user_info.password = $event.detail.value),
        g: common_vendor.p({
          type: "checkmarkempty",
          size: "24",
          color: "rgb(66,157,250)"
        }),
        h: user_info.sms_code,
        i: common_vendor.o(($event) => user_info.sms_code = $event.detail.value),
        j: common_vendor.o(userRegister)
      };
    };
  }
};
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["__scopeId", "data-v-bac4a35d"]]);
wx.createPage(MiniProgramPage);
//# sourceMappingURL=../../../.sourcemap/mp-weixin/pages/register/register.js.map
