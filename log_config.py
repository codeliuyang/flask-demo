'''
日志记录配置，默认输出到logs文件夹
且只能打印current_app.logging的日志
'''
import logging
from logging.handlers import TimedRotatingFileHandler
import time
import os


def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def log_format(app):
    log_dir = 'logs'
    log_file_name = log_dir + '/flask-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    make_dir(log_dir)
    handler = TimedRotatingFileHandler(
        log_file_name, when="D", interval=1, backupCount=15,
        encoding="UTF-8", delay=False, utc=True)
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)