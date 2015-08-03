"""
Output all the URL link in 'www.yahoo.com'
"""



import urllib2, re
 
url = "http://www.yahoo.com"
html_doc = urllib2.urlopen(url).read()
temp=re.findall('href="(.*?)"', html_doc)
num=0
while (num < len(temp)):
        if ('http' in temp[num]):
                print temp[num]
                num +=1
        else:
                num+=1
