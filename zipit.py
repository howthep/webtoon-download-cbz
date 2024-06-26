from zipfile import ZipFile
from glob import glob
import os
from crawl import webtoon
xinhun=812354
id=812356
id=xinhun
name=1
with open('number','r') as num:
    name = int(num.readline())
hua=name
webtoon(id,hua)

imgs = glob("*.jpg")
zip_name=f'{name}.zip'
print(zip_name)
with ZipFile(zip_name,'w')  as pszip:
    for img in imgs:
        pszip.write(img)

for img in imgs:
    os.remove(img)

with open('number','w') as num:
    num.write(f'{name+1}')