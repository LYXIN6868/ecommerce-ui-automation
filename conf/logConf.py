# 定义日志的基本操作
import logging
import os
from logging import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(BASE_DIR, 'logs'), exist_ok=True)

config.fileConfig(os.path.join(BASE_DIR, 'conf', 'log.conf'))
logger = logging.getLogger()
