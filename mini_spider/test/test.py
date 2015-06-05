

import re
a = ".*\.(gif|png|jpg|bmp)$"
partern = re.compile(a)
if partern.match("www.abc.com/dd.jpg"):
    print 1