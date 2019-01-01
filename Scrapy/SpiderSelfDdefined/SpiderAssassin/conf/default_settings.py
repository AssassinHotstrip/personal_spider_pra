#coding:utf-8

import sys
import logging

# 默认的配置
DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'   # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = 'log.log'    # 默认日志文件名称

# 当框架被导入到用户运行环境时，相当于将所有代码拷贝到了用户的运行环境中
# 相当于from settings import * 执行的时候 用户代码目录下的 settings
# 使用用户配置信息，替换框架默认配置信息
from settings import *
