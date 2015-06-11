# -*- coding:utf-8 -*-
# !/usr/bin/env python
################################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This module is the test class to test urlParse
"""
import unittest

from engine import UrlParse

class UrlParseTest(unittest.TestCase):
    """
    Test UrlPars
    """
    def setUp(self):
        self.url = "http://www.baidu.com"

    def test_get_urls(self):
        """
        test get urls in the original url
        :return: nothing
        """
        UrlParse.UrlParse.get_urls(self.url)

    def test_download(self):
        """
        test download url to file
        :return: nothing
        """
        UrlParse.UrlParse.download("D:\\test\\test", "https://www.baidu.com/")

    def test_get_html_content(self):
        """
        get the html code from from url
        :return: nothing
        """
        print UrlParse.UrlParse.get_html_content("https://www.baidu.com")

    def test_get_url(self):
        """
        test get urls in the original url
        :return: nothing
        """
        print UrlParse.UrlParse.get_urls("http://www.baidu.com")

    def test_is_url(self):
        """
        test check url
        :return:nothing
        """
        print UrlParse.UrlParse.is_url("javadscriptddddddd")