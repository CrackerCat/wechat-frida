from setuptools import setup, find_packages

setup(
    name='wechatf',
    version="0.0.1",
    description='core 微信机器人框架（自动聊天、http协议访问）。',
    long_description='core 使用frida框架hook微信PC端的python聊天机器人框架。（支持http调用、chatgpt聊天、自动回复好友消息等)。',
    author='luoyeah',
    author_email='dao696@foxmail.com',
    maintainer='',
    maintainer_email='',
    url='https://github.com/luoyeah/wechat-frida',
    license='MIT license',
    keywords=[
        '',
    ],
    platforms=["Windows"],
    # packages=['wechatf'],
    # packages=find_packages(),
    packages=['wechatf'],
    # packages=[p for p in find_packages() if p.startswith('wechatf')],
    # include all packages under automated
    # package_dir={'':'automated'},  # tell distutils packages are under automated
    include_package_data=True,
    install_requires=open("requirements.txt", 'r', encoding='utf-8').read().split("\n"),
    # tests_require=['coverage', 'pytest'],
    # extras_require={
    #     'ipython': ['ipython==6.21']
    # },
    # scripts=[
    #     './automated/bin/main.py',
    # ],
    entry_points={
        'console_scripts': [
            'wechatf-http-server = wechatf.wechatf_http_server_start:main',
            'wechatf-auto-chat = wechatf.wechatf_auto_chat:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Natural Language :: Chinese',
    ],
)
