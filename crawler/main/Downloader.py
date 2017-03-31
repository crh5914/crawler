import urllib2
from bs4 import BeautifulSoup
import re
class Downloader:
      def download(self,url):
          headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
          req= urllib2.Request(url,headers=headers)
          res = urllib2.urlopen(req)
          html = res.read()
         # print(html)

          #print(html)

          doc = BeautifulSoup(html,'html.parser')
          project = doc.find_all('li',attrs={"data-dropdown-group": "projects"})
          print(project)
      def formatCatergory(self,catergory):
           res = []
           for c in catergory:
              c = c.strip()
              c = c.lower()
              c = c.replace('&amp;','_')
              c = c.replace(' ','_')
              res.append(c)
           return res

      def getLabels(self,catergory):
          print('asbsdjk')


if __name__=='__main__':
    d = Downloader()
    catergory = ['Hello world ','Java&amp;PHP',' hello world']
    print(d.formatCatergory(catergory))
    print(catergory)
    #d.download('http://www.archdaily.com/')