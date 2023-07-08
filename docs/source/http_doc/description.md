### 特性

1. 使用frida框架hook微信PC客户端，便于调试js代码和快速适配最新客户端。
2. 根据系统已安装微信版本自动加载与其对应的frida js脚本。
3. 可自行在```wechatf/js/```文件夹下添加最新版本适配脚本。
4. 提供http协议访问接口。
5. 可设置自动回复好友消息内容、开启和关闭自动回复、ChatGPT聊天功能。
### 快速开始
1. 下载并安装```v3_2_1_154```版本的微信。 （自行搜索下载，或点击这里：[WeChatSetup-3.2.1.154.exe](https://www.dngswin10.com/pcrj/15.html)下载，请注意核对数字签名是否正常）
2. 安装python3.8及以上版本,下载地址:[https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
3. 安装、运行。
```bash
pip install wechatf

# 启动服务，默认本地8001端口
wechatf-http
```