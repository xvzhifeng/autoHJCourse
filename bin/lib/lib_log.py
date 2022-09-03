# -*- coding:utf-8 -*-
import os
import yaml
import logging
import logging.config

logger = None
log_path = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))), "conf/logging.yml")


def __init__():
    log_set_up()


def log_set_up():
    global logger
    global log_path
    print("log config file path : " + log_path)
    with open(log_path, 'r', encoding="utf-8") as f_conf:
        dict_conf = yaml.load(f_conf, Loader=yaml.FullLoader)
    for subHandlers in dict_conf['handlers']:
        for sub in dict_conf['handlers'][subHandlers]:
            if sub == 'filename':
                path = os.path.join(
                    os.path.dirname(
                        os.path.abspath(__file__)), dict_conf['handlers'][subHandlers][sub])
                dict_conf['handlers'][subHandlers][sub] = path
    logs = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'logs')
    if not os.path.exists(logs):
        os.mkdir(logs)
    logging.config.dictConfig(dict_conf)
    logger = logging.getLogger('simpleExample')


def debug(msg):
    global logger
    logger.debug(msg)


def info(msg):
    logger.info(msg)


log_set_up()
