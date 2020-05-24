#爬虫爬取指定关键词，指定页数百度搜索内容标题
#构建百度搜索URL网址，分析网页源码并构建正则表达式
#创建文件来保存爬虫爬取内容
#构建用户代理进行浏览器伪装，避免百度反爬虫机制



#加载URLlib，requests，正则，随机提取模块
import urllib.request
import requests
import random
import re





#构建用户代理池
UApools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    ]





#输入创建爬虫关键词，页码信息
#输入关键词并编码
keyword=input("请输入爬取关键词:")
key=urllib.request.quote(keyword)

#输入爬虫所爬百度搜索指定网页
pagenumbegin = input("请输入爬取起始页数(数字):")
pagenumend = input("请输入爬取结束页数(数字):")





#创建文档用于保存爬虫文件
#输入所保存文件名
filename = input("请输入创建文档名字:")

# 创建文件的存放路径，(默认存放D盘)
filelocation = "D:\\"

# 创建文件并定义格式
fileformat = filelocation + filename + '.txt'
file = open(fileformat, 'w')





#爬取网页数据，正则提取信息，打印并保存于文件
#打开所创建文件
fh = open("D:\\"+str(filename)+".txt","a")

#爬取多网页数据
for i in range(int(pagenumbegin)-1,int(pagenumend)):
    
    #随机抽取用户代理池并构建用户信息
    UA=random.choice(UApools)
    print(UA)
    headers = {
        "User-Agent":UA
    }
    
    #构建网址(代入关键词和页数)
    URL = "https://www.baidu.com/s?wd="+key+"&pn="+str((i-1)*10)
    
    #request爬虫获取数据
    data = requests.get(URL,headers = headers)
    
    #构建正则表达式
    pat1='"title":"(.*?)",'
    pat2="title:'(.*?)',"
    title1 = re.compile(pat1).findall(data.text)
    title2 = re.compile(pat2).findall(data.text)
    
    #输出所爬页码与标题
    print(str(i+1))
    print(str(i+1),file=fh)
    for j in range(0,len(title1)):
        print(title1[j])
        print(title1[j],file=fh)
    for k in range(0,len(title2)):
        print(title2[k])
        print(title2[k],file=fh)
    print('\n')
    print('\n',file=fh)

#关闭文件以保存爬取内容
fh.close()
