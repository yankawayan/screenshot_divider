from PIL import Image
import numpy as np

name_image = "img1.png"
path_image = "img\\"+name_image

"""
一般的なA4サイズ用紙のピクセル数
72dpi(72 dot per inch)
595px 842px

350dpi(350 dot per inch)
2894px 4093px
"""

# 元となる画像の読み込み
img = Image.open(path_image)
#オリジナル画像の幅と高さを取得
width, height = img.size
# オリジナル画像と同じサイズのImageオブジェクトを作成する
img2 = Image.new('RGB', (width, height))
print(width,height)

img_crop = img.crop((60, 20, 400, 200))
img_crop.show()