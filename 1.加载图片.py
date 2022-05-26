"""
name：1.加载图片
date:
author:liu.liang
"""
from PIL import Image
image =Image.open('./image/lufei.jpg')
print(image)
# image.show()
print(image.size, image.mode)
print(image.format)
print(image.info)
image.save