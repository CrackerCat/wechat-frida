"""
wechatf_http_server http服务启动器
"""
import uvicorn

if __name__ == '__main__':
    # uvicorn.run("wechatf_http_server:app", host='127.0.0.1', port=8001,reload=True, workers=1)
    uvicorn.run("wechatf_http_server:app", host='127.0.0.1', port=8001, workers=1)

# 命令行可直接启动
# uvicorn wechatf_http_server:app --reload
