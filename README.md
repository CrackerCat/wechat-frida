# [wechat-frida](https://github.com/luoyeah/wechat-frida)

## 1、介绍

* wechat-frida 是一款使用frida框架hook微信PC端的python聊天机器人框架。（支持http调用、chatgpt聊天、自动回复好友消息等)。
* 涉及技术：二进制逆向分析、frida动态hook、python、fastapi。
* 仓库地址：[https://github.com/luoyeah/wechat-frida](https://github.com/luoyeah/wechat-frida)
* 开发文档：[https://wechat-frida.readthedocs.io/zh_CN/latest/](https://wechat-frida.readthedocs.io/zh_CN/latest/)

## 2、特性

1. 使用frida框架js脚本hook微信电脑版客户端，方便适配最新版本客户端（frida-js目录：```wechatf/js/```）。
2. 提供http协议接口（[接口文档](https://wechat-frida.readthedocs.io/zh_CN/latest/)）。
3. 可设置自动回复好友消息内容、开启和关闭自动回复、ChatGPT聊天功能。

## 3、快速开始

### 3.1 安装

1. 下载并安装```v3_2_1_154```版本的微信。
   （自行搜索下载，或点击这里：[WeChatSetup-3.2.1.154.exe](https://www.dngswin10.com/pcrj/15.html)下载，请注意核对数字签名是否正常）
2. 安装python3.8及以上版本,下载地址:[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

3. 安装。

```bash
pip install wechatf
```

### 3.2、http协议访问

1. 启动服务

```bash
wechatf-http
```

2. API默认地址：http://127.0.0.1:8001
3. API接口文档：[https://wechat-frida.readthedocs.io/zh_CN/latest/](https://wechat-frida.readthedocs.io/zh_CN/latest/)

### 3.3、自动回复消息、GPT聊天

1. 免费获取ChatGPT访问key，获取地址 ：[https://github.com/chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free)
，跳转到链接后，点击```领取免费Key```链接，使用github账号授权获取key。

2. 运行

> 首次会提示输入ChatGPT访问key

```bash
wechatf-chat
```

3. 用手机微信向文件传输助手发送```/h```命令获取帮助：

 ```bash
/h
打印帮助消息。

/sa msg
开启自动回复并设置内容。

/ea
取消自动回复。

/sai
开启ai聊天。

/cai
清除ai聊天上下文

/eai
取消ai聊天。
 ```

4. 用手机微信向文件传输助手发送消息可实现向GPT聊天。

###  3.4、python脚本中使用

```python
# 导入包
import wechatf

# 发送消息
wxid = "filehelper"  # 文件传输助手
message = "你好"
wechatf.send_message(wxid, message)

# 获取消息 以阻塞模式获取
msg = wechatf.get_message()
print(msg)

# 获取所有联系人
contacts = wechatf.get_contacts()
print(contacts)
```

## 4、支持版本和功能

#### ✅v3_2_1_154_x86

* ✅ 获取登录状态
* ✅ 获取登录二维码
* ✅ 获取登录信息
* ✅ 退出微信
* ✅ 获取联系人列表
* ✅ 接收文本消息
* ✅ 发送文本消息

#### 🚧v3_9_5_80_x86

* ⬜ 获取登录状态
* ⬜ 获取登录二维码
* ⬜ 获取登录信息
* ⬜ 退出微信
* ⬜ 获取联系人列表
* ✅ 接收文本消息
* ✅ 发送文本消息

## 5、参与贡献

1. Fork 本仓库
2. 新建 dev 分支
3. 提交代码
4. 新建 Pull Request

-----------------------------------
注：该程序仅用于学习交流，禁止商用或其他非法用途。
