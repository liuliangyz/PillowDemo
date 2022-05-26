"""
name：5.自定义一张图片
date:
author:liuliang
"""
from PIL import Image
img = Image.new('RGB', (400, 400), color=(0, 255, 0))
img.show()