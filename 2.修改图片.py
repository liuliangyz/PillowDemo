"""
name：2.修改图片
date:
author:liuliang
"""
# from PIL import Image
# image = Image.open('./image/lufei.jpg')
# print(image.size)
# image1 = image.resize((image.size[0]//2, image.size[1]//2))
# image1.show()
# image1.save('./image/small_lufei.jpg')

from PIL import Image, ImageDraw, ImageFont
img = Image.open('./image/lufei.jpg')
draw = ImageDraw.Draw(img)
# draw.text((10, 10), 'liuliang')
cus_font = ImageFont.truetype('./font/PingFang.ttc')
draw.text((30, 30), '版权：刘亮', font=cus_font, fill=(255, 255, 255))
img.show()