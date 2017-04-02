#Created on 2017/4/2
#@author: crh
from bs4 import BeautifulSoup
class InfoExtraction:
    def extractdirs(self,html):
        doc = BeautifulSoup(html,'html.parser')
        catdoc = doc.find_all('li',{'data-dropdown-group':'projects'})
        cats = {}
        #doc = BeautifulSoup(catdoc)
        for cat in catdoc:
            label = cat.a.text
            label = self.formatlabel(label)
            cats[label]={}
            #print label
            selector = '#%s-box li a'%label
            #print selector
            subcats = doc.select(selector)
            #print '%s(%d)'%(label,len(subcats))
            for subcat in subcats:
                if 'afd-flyout__featured__link' in subcat.get('class'):
                    continue
                subcatlabel = subcat.text
                subcatlabel = self.formatlabel(subcatlabel)
                cats[label][subcatlabel] = subcat['href']
                #print '      %s'%subcatlabel
        return cats  
    def formatlabel(self,label):
        label = label.lower()
        label = label.replace(' ','-')
        label = label.replace('-&-','-')
        return label
    def getpagenum(self,html):
        doc = BeautifulSoup(html,'html.parser')
        a = doc.select_one('a.last')
        href = a['href']
        pagenum = None
        if href == None:
            pagenum = 1
        else: 
            if len(href and '>page=')>0:                  
                pagenum = int(href[href.index('=')+1:])
            else:
                pagenum = 1
        return pagenum