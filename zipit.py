from zipfile import ZipFile
from glob import glob
import os
from crawl import webtoon
xinhun=812354
samguk=711422
holangi=650305
pandag=61731
id=812356
id=pandag
name=1
with open('number','r') as num:
    name = int(num.readline())

def img_zip(imgs,name):
    suffix='cbz'
    zip_name=f'{name}.{suffix}'
    print(zip_name)
    with ZipFile(zip_name,'w')  as pszip:
        for img in imgs:
            pszip.write(img)

hua_len = 2
dir='pandag'
if not os.path.exists(dir):
    os.makedirs(dir)
for i in range(hua_len):
    print(f'{i}/{hua_len}')
    imgs=[]
    cnt=0
    while len(imgs)<=0:
        if cnt>1:
            print(f'{name} hua not get, try again,{cnt}')
        webtoon(id,name)
        imgs = glob("*.jpg")
        cnt+=1
    zip_name = os.path.join(dir,str(name))
    img_zip(imgs,zip_name)
    name+=1
    for img in imgs:
        os.remove(img)
    with open('number','w') as num:
        num.write(f'{name}')
