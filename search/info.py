#-*- coding:utf8 -*-

import requests
import json
import pprint
import re


INFO_URL = 'https://www.kujiale.com/3dm/api/search?'

class ModelInfo(object):
    
    def __init__(self, url, params):
        self.url = url
        self.params = params
    
    def get_context(self):
        
        r = requests.get(self.url, params=self.params)
        text = r.text.replace(r'"','')

        urls = re.findall( r'url:(.+?),', text)
        imgs = re.findall( r'img:(.+?),', text)
        # versions = re.findall(r"version:(.+?)[,|']",text)
        names = re.findall(r"name:(.+?)[,|'|}]", text)
        count = re.findall(r'count:(.+?),', text)

        index = 0
        packages = []
        while index < len(urls):
            
            package = {
                'url':urls[index],
                'img':imgs[index],
                'name':names[index]
            }

            packages.append(package)
            index = index+1

        context = {
            'word':self.params['word'],
            'source':self.params['source'],
            'count':count[0],
            'packages':packages
        }

        return context 

if __name__ == '__main__':
    
    params = {
        'url':INFO_URL,
        'data':{
            'word':'水',
            'start':'0',
            'num':'2',
            'source':'3'
        }
    }
    info = ModelInfo(params['url'], params['data']).get_context()
    pprint.pprint(info)

    # for i, j in [ [1,3] , [4,5]]:
    #     print(i, j)



# url = 'https://www.kujiale.com/3dm/search?'



# r = requests.get(url, params=params)

# print(r.url)

# with open('1.html', 'wb') as fd:
#     for chunk in r.iter_content(100):
#         fd.write(chunk)

# text = open('1.html', 'r',encoding='utf8').read()


# pattern = 'model = \{(.+?)\}'
# urls = re.findall(pattern, text, re.S)

# # print(urls)

# infos = list()
# for url in urls:
#     info = list()
#     temp = url.split('\n')
#     info.append(temp[1].strip()[6:-3])
#     info.append(temp[2].strip()[6:-3])
#     info.append(temp[3].strip()[10:-2])
#     info.append(temp[4].strip()[7:-2])
#     infos.append(info)

# for info in infos:
#     print(info)
    