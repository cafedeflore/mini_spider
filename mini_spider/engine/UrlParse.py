# -*- coding:utf-8 -*-
# !/usr/bin/env python
################################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
This module is some static method for parse url, html
"""
import os
import urllib
import urllib2
import urlparse
import logging

import chardet
from bs4 import BeautifulSoup


class UrlParse(object):
    """
    the public url tools to deal with url
    """

    @staticmethod
    def is_url(url):
        """
        if the url is start with javascript ignore it
        :param url:
        :return:True False
        """
        if url.startswith("javascript"):
            return False
        return True

    @staticmethod
    def get_urls(url):
        """
        get the urls under this url
        :param url: origin url
        :return:the set of sub_urls
        """
        url_set = set()
        if not UrlParse.is_url(url):
            return url_set

        content = UrlParse.get_html_content(url)
        if content is None:
            return url_set
        tag_list = ['img', 'a', 'script', 'style']
        link_list = []

        for tag in tag_list:
            link_list.extend(BeautifulSoup(content).findAll(tag))

        for link in link_list:
            if link.has_attr('src'):
                url_set.add(UrlParse.deal_with_url(link['src'], url))
            if link.has_attr('href'):
                url_set.add(UrlParse.deal_with_url(link['href'], url))
        # print url_set
        return url_set

    @staticmethod
    def deal_with_url(url, base_url):
        """
        deal with url to make it complete and standard
        :param url: the url href
        :param base_url: the base url where the orginal url is
        :return:completed url
        """
        if url.startswith('http') or url.startswith('//'):
            url = urlparse.urlparse(url, scheme='http').geturl()
        else:
            url = urlparse.urljoin(base_url, url)
        return url

    @staticmethod
    def get_html_content(url, timeout=10):
        """
        Get html contents
        :param url: the target url
        :param timeout: urlopen timeout, default 10
        :return: the content of html page, return None when error happens
        """
        try:
            response = urllib2.urlopen(url, timeout=timeout)
        except urllib2.URLError as err:
            logging.error("url open error : %s" % url)
            return None
        try:
            content = response.read()
        except Exception as err:
            logging.error("read response error")
            return None

        return UrlParse.decode_html(content)

    @staticmethod
    def decode_html(content):
        """
        decode content
        :param content: the origin content
        :return: returen decoded content. Error return None
        """
        encoding = chardet.detect(content)['encoding']
        if encoding == 'GB2312':
            encoding = 'GBK'
        else:
            encoding = 'utf-8'
        try:
            content = content.decode(encoding, 'ignore')
        except Exception as err:
            logging.error("Decode error: %s.", err)
            return None
        return content

    @staticmethod
    def download(local_path, url):
        """
        download html, file to local file
        :param local_path: base_path
        :param url: download url
        :return: succeed True, fail False
        """

        if not os.path.exists(local_path):
            try:
                os.mkdir(local_path)
            except os.error as err:
                logging.error("download to path, mkdir errror: %s" % err)

        try:
            path = os.path.join(local_path, url.replace('/', '_').replace(':', '_')
                                .replace('?', '_').replace('\\', '_'))
            logging.info("download url..: %s" % url)
            urllib.urlretrieve(url, path, None)
        except Exception as err:
            logging.error("download url fail. url: %s" % url)
            return False
        return True