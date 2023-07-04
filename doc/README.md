# sphinx文档生成

## 1、安装依赖
```python
pip install sphinx sphinx-autobuild sphinx_rtd_theme recommonmark sphinx-markdown-tables
```
## 2、创建模板
```python
sphinx-quickstart
```

## 3、更改conf.py
```python
html_theme = "sphinx_rtd_theme"
extensions = ['recommonmark']
```