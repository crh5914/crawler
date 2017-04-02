#Created on 2017/4/2
#@author: crh
import urllib2
class Downloader:
    def __init__(self,headers):
        self.headers = headers
    def download(self,url):
        print url
        req = urllib2.Request(url,headers=self.headers)
        res = urllib2.urlopen(req)
        html = res.read()
        return html 