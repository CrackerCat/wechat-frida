
# [wechat-frida](https://github.com/luoyeah/wechat-frida) PC微信聊天机器人框架 （支持GPT聊天、自动回复好友消息、Http协议访问)
## 1、介绍
* wechat-frida 是一款使用frida框架hook微信PC端的聊天机器人框架。该框架使用frida js脚本动态hook程序，便于调试和快速适配最新客户端。
* 仓库地址：[https://github.com/luoyeah/wechat-frida](https://github.com/luoyeah/wechat-frida)
* 涉及技术：二进制逆向分析、frida动态hook、python、fastapi

## 2、特性

1. 使用frida框架hook微信PC客户端，便于调试js代码和快速适配最新客户端。
2. 根据系统已安装微信版本自动加载与其对应的frida js脚本。
3. 可自行在```wechatf/js/```文件夹下添加最新版本适配脚本。
4. 提供http协议访问接口。
5. 可设置自动回复好友消息内容、开启和关闭自动回复、ChatGPT聊天功能。
## 3、快速开始
### 3.1 安装
1. 下载并安装```v3_2_1_154```版本的微信。 （自行搜索下载，或点击这里：[WeChatSetup-3.2.1.154.exe](https://www.dngswin10.com/pcrj/15.html)下载，请注意核对数字签名是否正常）
2. 安装python3.8及以上版本,下载地址:[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
4. 拉取代码并安装依赖。
```bash
# 代码克隆到本地
git clone https://github.com/luoyeah/wechat-frida

# 切换到代码目录
cd wechat-frida

# 安装依赖
pip install -r requirements.txt
```
###  3.2、使用自动聊天功能
1. 获取ChatGPT访问key，免费获取地址 ：[https://github.com/chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free)，跳转到链接后，再点击```免费获取```链接，使用github账号授权获取key。
2. 在项目根目录新建```openai.key```文件，将key保存此文件。
3. 运行auto_repeat.py。

```bash
# 切换到代码目录
cd wechat-frida

# 运行
python auto_repeat.py
```
4. 用手机微信向文件传输助手发送```/h```命令获取帮助：
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
### 3.3、http协议访问

1. 运行程序
```bash
# 切换到代码目录
cd wechat-frida

# 运行
python wechatf_fastapi.py
```
2. api接口端口：http://127.0.0.1:8000
3. 功能列表
```bash
查询是否登录
GET /is_login

获取登录二维码
GET /get_login_qrcode

获取用户信息
GET /get_user_info

退出登录
GET /logout

获取所有联系人
GET /get_contacts

获取一条文本消息
GET /get_message

发送文本消息
GET /send_message/{wxid}/{content}
```
查看更多：[https://github.com/luoyeah/wechat-frida/docs/](https://github.com/luoyeah/wechat-frida/docs/)
## 4、在脚本中使用
```python
# 导入包
import wechatf

# 发送消息
wechatf.send_message(wxid, msg)

# 获取消息 以阻塞模式获取
msg= wechatf.get_message()

# 获取联系人
contacts = wechatf.get_contacts()
```

## 5、支持版本功能

#### v3_2_1_154

* ✅ 获取登录状态
* ✅ 获取登录二维码
* ✅ 获取登录信息
* ✅ 获取联系人列表
* ✅ 接收文本消息
* ✅ 发送文本消息
* ✅ 退出微信

#### v3_9_5_80 (x86)

* ✅ 接收文本消息
* ✅ 发送文本消息
* ⬜ 获取联系人列表（🚧施工中）
* ⬜ 获取登录二维码🚧
* ⬜ 获取个人信息、登录状态🚧


##  6、参与贡献

1.  Fork 本仓库
2.  新建 dev 分支
3.  提交代码
4.  新建 Pull Request

-----------------------------------
注：该程序仅用于学习交流，禁止商用或其他非法用途。