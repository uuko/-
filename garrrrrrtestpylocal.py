import urllib.request
from bs4 import BeautifulSoup
#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
httmml = urllib.request.Request(url="http://localhost/title.php" ,headers=headers)
page = urllib.request.urlopen(httmml).read()
soup = BeautifulSoup(page, "html.parser")
# req = urllib.request.Request(url=aurl, headers=headers)
# response=urllib.request.urlopen(req).read()
# soup =  BeautifulSoup(response,"html.parser")
container1=soup.select('body')[0]
print(container1)