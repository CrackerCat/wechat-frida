wechat-frida
========================================

* wechat-frida 是一款使用frida框架hook微信PC端的聊天机器人框架。该框架使用frida js脚本动态hook程序，便于调试和快速适配最新客户端。
* 仓库地址：https://github.com/luoyeah/wechat-frida
* 涉及技术：二进制逆向分析、frida动态hook、python、fastapi

.. toctree::
   :maxdepth: 1
   :caption: API接口列表:

   api_doc/01 获取登录状态.md
   api_doc/02 获取登录二维码.md
   api_doc/03 退出登录.md
   api_doc/04 获取所有联系人.md
   api_doc/05 获取一条文本消息.md
   api_doc/06 发送一条文本消息.md
