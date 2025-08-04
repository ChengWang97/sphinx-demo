# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SphinxTest'
copyright = '2025, WangCheng'
author = 'WangCheng'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc', #文档自动生成
    'sphinx.ext.viewcode',#在文档中显示源代码
    'sphinx.ext.intersphinx',#链接到其他Sphinx文档的链接
    'sphinx.ext.todo',#TODO列表
    'sphinx.ext.coverage',#覆盖率报告
    'sphinx_copybutton',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_search_language = 'zh'
html_title = '河北医大超算平台用户手册'