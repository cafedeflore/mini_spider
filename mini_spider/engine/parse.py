# coding=utf-8\
import urllib
import urllib2
import re
import os
from bs4 import BeautifulSoup

class parse:

    @staticmethod
    def _is_url(url):
        if url == "javascript:;":
            return False
        return True

    @staticmethod
    def get_urls(url):
        response = None
        content = None
        res = []
        try:
            response = urllib2.urlopen(url, timeout=10)
            content = response.read()
        except Exception as e:
            raise e

        a = re.compile(r'href="([^"]*)"').findall(content)
        for i in a:
            if parse._is_url(i):
                res.append(i)
        return res

    @staticmethod
    def get_files(url, regex):
        response = None
        content = None
        res = []
        try:
            response = urllib2.urlopen(url, timeout=10)
            content = response.read()
        except Exception as e:
            raise e

        b = re.compile(r'(http://[A-Za-z0-9_\./?&=]*.(js|png|jpg$))').findall(content)
        for i in b:
            res.append(i[0])
        return res

    @staticmethod
    def download(local_path, url):
        try:
            path = os.path.join(local_path, url.split('/')[-1])
            urllib.urlretrieve(url, path, None)
        except Exception as e:
            print e
            print "error"

parse.get_files("http://www.baidu.com", "")