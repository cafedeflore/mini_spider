# -*- coding:utf-8 -*-
# !/usr/bin/env python
################################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This module contains global variable for default conf
"""
import log
import logging
import unittest

from engine import SpiderEngine

class UrlParseTest(unittest.TestCase):
    """
    Test UrlPars
    """
    def setUp(self):
        self.url = "http://www.baidu.com"

    def test_engine(self):
        log.init_log("D:\\test\\test\\log")  # 日志保存到./log/my_program.log和./log/my_program.log.wf，按天切割，保留7天
        logging.info("Hello World!!!")
        a = SpiderEngine.SpiderEngine()
        a.set_config_by_file("D:\work\python\mini_spider\mini_spider\mini_spider\spider_conf")
        a.start_work()