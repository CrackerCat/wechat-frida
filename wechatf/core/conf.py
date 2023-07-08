"""
配置文件
"""

# 支持版本
support_version = {
    # 版本号
    "v3_2_1_154_x86": {
        # 需要预先注册的frida-js，一般用于hook特定函数，在函数被调用时主动发送send消息给python的on_message回调函数
        "frida_recv_js": [
            "recv_login_qrcode",
            "recv_friend_list",
            "recv_message",
        ],
    },
}
