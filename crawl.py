import requests
import urllib
from bs4 import BeautifulSoup as bs
from io import StringIO
from PIL import Image
import os
def webtoon(id,hua):
    '''
    id: unique for manhua
    hua: 1,2,3,...
    '''
    UA= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    # UA='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': UA,
        'sec-ch-ua-platform': '"Windows"',
    }
    url=f'https://comic.naver.com/webtoon/detail?titleId={id}&no={hua}'
    r = requests.get(url,headers=headers)
    soup=bs(r.text,'html.parser')
    wt = soup.find('div',class_='wt_viewer')
    # print(wt)
    imgs= wt.find_all('img',recursive=False)
    for i,img in enumerate(imgs):
        img_url=img['src']
        # some webtoon suffix is gif, dnot know why
        # if not img_url.endswith("jpg"):
        #     continue
        if img_url.find(str(id)) <0 :
            continue
        print(img_url)
        r=requests.get(img_url,headers=headers)
        # print(r.content)
        img_name=f'img_{i}.jpg'
        with open(img_name,'wb') as f:
            f.write(r.content)
        # i=Image.open(img_name)
        # w,h=i.size
        # if w>h:
        #     i.close()
        #     os.remove(img_name)
