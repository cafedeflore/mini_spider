# -*- coding:utf-8 -*-
# !/usr/bin/env python
################################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This module is the test class to test spiderengine
author linnan01(com@baidu.com)
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
        """
        test engine works well
        :return: nothing
        """
        a = SpiderEngine.SpiderEngine()
        a.set_config_by_file("../spider_conf")
        a.start_work()

    def test_set_config(self):
        """
        test the engine's setting config
        :return: nothing
        """
        a = SpiderEngine.SpiderEngine()
        a.set_config("urls", "output", 1, 1, 1, "*\.(html|png|jpg|bmp)$", 1)

    def test_url_leaf(self):
        """
        test the UrlLeaf class
        :return:nothing
        """
        leaf = SpiderEngine.UrlLeaf('lalal', 0)
        print leaf