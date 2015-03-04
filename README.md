在调研过程中，经常需要对一些网站进行定向抓取。由于python包含各种强大的库，使用python做定向抓取比较简单。请使用python开发一个迷你定向抓取器mini_spider.py，实现对种子链接的广度优先抓取，并把URL长相符合特定pattern的网页保存到磁盘上。
程序运行: 
python mini_spider.py -c spider.conf 

配置文件spider.conf: 
[spider] 
url_list_file: ./urls ; 种子文件路径 
output_directory: ./output ; 抓取结果存储目录 
max_depth: 1 ; 最大抓取深度(种子为0级) 
crawl_interval: 1 ; 抓取间隔. 单位: 秒 
crawl_timeout: 1 ; 抓取超时. 单位: 秒 
target_url: .*\.(gif|png|jpg|bmp)$ ; 需要存储的目标网页URL pattern(正则表达式) 
thread_count: 8 ; 抓取线程数 

种子文件每行一条链接，例如: 
http://www.baidu.com 
http://www.sina.com.cn 

要求和注意事项: 
需要支持命令行参数处理。具体包含: -h(帮助)、-v(版本)、-c(配置文件)

需要按照广度优先的顺序抓取网页。

单个网页抓取或解析失败，不能导致整个程序退出。需要在日志中记录下错误原因并继续。

当程序完成所有抓取任务后，必须优雅退出。

从HTML提取链接时需要处理相对路径和绝对路径。

需要能够处理不同字符编码的网页(例如utf-8或gbk)。

网页存储时每个网页单独存为一个文件，以URL为文件名。注意对URL中的特殊字符，需要做转义。

要求支持多线程并行抓取。

代码严格遵守百度python编码规范

代码的可读性和可维护性好。注意模块、类、函数的设计和划分

完成相应的单元测试和使用demo。你的demo必须可运行，单元测试有效而且通过

注意控制抓取间隔和总量，避免对方网站封禁百度IP。PS Python CM委员会为大家提供测试抓取网站: http://pycm.baidu.com:8081


提示(下面的python库可能对你完成测试题有帮助): 

re(正则表达式)
参考: http://docs.python.org/2/library/re.html

参考: http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html

参考: http://blog.csdn.net/jgood/article/details/4277902


gevent/threading(多线程)
参考: http://docs.python.org/2/library/threading.html

参考: http://www.cnblogs.com/huxi/archive/2010/06/26/1765808.html

docopt/getopt/argparse(命令行参数处理)
参考: https://github.com/docopt/docopt

参考: http://docs.python.org/2/library/getopt.html

参考: http://andylin02.iteye.com/blog/845355

参考: http://docs.python.org/2/howto/argparse.html

参考: http://www.cnblogs.com/jianboqi/archive/2013/01/10/2854726.html

ConfigParser(配置文件读取)
参考: http://docs.python.org/2/library/configparser.html

参考: http://blog.chinaunix.net/uid-25890465-id-3312861.html

urllib/urllib2/httplib(网页下载)
参考: http://docs.python.org/2/library/urllib2.html

参考: http://blog.csdn.net/wklken/article/details/7364328

参考: http://www.nowamagic.net/academy/detail/1302872

pyquery/beautifulsoup4/HTMLParser/SGMLParser(HTML解析)
参考: http://docs.python.org/2/library/htmlparser.html

参考: http://cloudaice.com/yong-pythonde-htmlparserfen-xi-htmlye-mian/

参考: http://docs.python.org/2/library/sgmllib.html

参考: http://pako.iteye.com/blog/592009

urlparse(URL解析处理)
参考: http://docs.python.org/2/library/urlparse.html

参考: http://blog.sina.com.cn/s/blog_5ff7f94f0100qr3c.html

logging(日志处理)
参考: http://docs.python.org/2/library/logging.html

参考: http://kenby.iteye.com/blog/1162698

参考: http://my.oschina.net/leejun2005/blog/126713
