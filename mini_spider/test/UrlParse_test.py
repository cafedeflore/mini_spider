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
import unittest

from engine import UrlParse

class UrlParseTest(unittest.TestCase):
    """
    Test UrlPars
    """
    def setUp(self):
        self.url = "http://www.baidu.com"
        # self.url = "http://pycm.baidu.com:8081/"

    def test_get_urls(self):
        # a = UrlParse.UrlParse()
        UrlParse.UrlParse.get_urls(self.url)

    def test_download(self):
        # a = UrlParse.UrlParse()
        UrlParse.UrlParse.download("D:\\test\\test", "https://www.baidu.com/")

    def test_get_html_content(self):
        # print UrlParse.UrlParse.get_html_content("https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/"
        #                                          "static/superplus/img/logo_white_ee663702.png")
        print UrlParse.UrlParse.get_html_content("https://www.baidu.com")

    def test_get_url(self):
        # print UrlParse.UrlParse.get_html_content("https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/"
        #                                          "static/superplus/img/logo_white_ee663702.png")
        print UrlParse.UrlParse.get_urls("http://www.baidu.com")