# -*- coding: utf-8 -*-
import os
import collections

urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

def getTopFileName(urlList, topRank):
    
    url_dict = collections.defaultdict(int)
    for url in urlList:
        basename = os.path.basename(url)
        url_dict[basename] = url_dict[basename] + 1

    sorted_dict = sorted(url_dict.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_dict[0:topRank]

top_urls = getTopFileName(urls, 3)

for url in top_urls:
    print(str(url[0])+' '+str(url[1]))