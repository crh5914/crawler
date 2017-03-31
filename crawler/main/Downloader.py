import urllib2
from bs4 import BeautifulSoup
class Downloader:
      def download(self,url):
          headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
          req= urllib2.Request(url,headers=headers)
          res = urllib2.urlopen(req)
          html = res.read()
          #print(html)
          doc = BeautifulSoup(html,'html.parser')
          a = doc.find_all(href='http://www.archdaily.com/search/projects')
          print(a[1])
          ul = a[1].next_siblings
          print(ul)
         # print(res.read())


if __name__=='__main__':
    d = Downloader()
    d.download('http://www.archdaily.com/')