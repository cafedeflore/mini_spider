# -*- coding:utf-8 -*-
# !/usr/bin/env python
################################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This main module
"""
import getopt
import log
import logging
import sys

from engine import SpiderEngine


def version():
    """
    print the version
    """
    print "version 1.0.0"


def main():
    """
    the main method to run mini spider
    """
    # 日志保存到./log/spider.log和./log/spider.log.wf，按天切割，保留7天
    log.init_log("./log/spider")
    spider = SpiderEngine.SpiderEngine()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vhc:")
    except getopt.GetoptError as err:
        logging.error("get option error : %s." % err)
        return
    for o, a in opts:
        if o == "-v":
            version()
            return
        elif o == "-h":
            # spider_engine = _SpiderEngine._SpiderEngine()
            # spider_engine.config_tostring()
            # spider_engine.set_config()
            print "帮助信息：没有帮助^_^"
            return
        elif o == "-c":
            spider.set_config_by_file(a)
        else:
            logging.error("unhandled option")
            print "unhandled option"
            return
    spider.start_work()
    return

if __name__ == "__main__":
    main()
# print "hello world!"