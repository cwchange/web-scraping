"""
For more information, take a look at my blog

https://cwchange.wordpress.com/2015/07/23/python-basic-web-login-script/

"""


import urllib, urllib2, cookielib
 
‪#‎create‬ a cookie file to store the cookie

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
 
‪#‎pass‬ the login information to the opener

login_data = urllib.urlencode({’username’ : your_username, ‘password’ : your_password,’submit’ : ‘Submit’, ‘id’: ‘U45i83’ })
 
‪#‎replace‬ the “the_login_url” to the url that require login, example:http://example.com/login.php

resp = opener.open(“the_login_url”, login_data)
#resp= opener.open("www.example.com/lgoin.php", login_data)
 
‪#‎You‬ can print the output, the output will be in HTML

print resp.read()
 
‪#‎going‬ to other url which share the same cookie

data=opener.open(“another url”)
