#Created on 2017/4/2
#@author: crh
import Downloader
import InfoExtraction
import os
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
url = 'http://www.archdaily.com'
d = Downloader.Downloader(headers)
ie = InfoExtraction.InfoExtraction()
html = ''
try:
    f = open('index.html')
    html = f.read()
    f.close()
except IOError,e:
    html = d.download(url)
    f = open('index.html','w')
    f.write(html)
    f.flush()
    f.close()
    print 'get index.html from web'
else:
    print 'Read index.html from filesystem'
#ie.extractdirs(html)
link = '<a class="last" href="/search/projects/categories/theater?page=6"></a>'
print ie.getpagenum(link)