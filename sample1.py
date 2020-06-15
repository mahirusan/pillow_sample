from PIL import Image,ImageDraw

# 背景となる画像(図形を描画する画像)のImageオブジェクトを準備し、
# それを使ってDrawオブジェクトを生成する

# Image.new()でベタ画像を作成
# モード、サイズ、塗りつぶす色を引数で指定
img1 = Image.new('RGB',(500,300),(128,128,128))
draw1 = ImageDraw.Draw(img1)



# Drawオブジェクトの図形描画メソッドを呼び出して図形を描画する
# 例として楕円、四角、直線を描画する
draw1.ellipse((100,100,150,200),fill=(255,0,0),outline=(0,0,0))
draw1.rectangle((200,100,300,200),fill=(0,192,192),outline=(255,255,255))
draw1.line((350,200,450,100),fill=(255,255,0),width=10)

img1.save('data/dst/pillow_imagedraw.jpg',quality=95)

def image_create():
    img2 = Image.new('RGB',(500,300),(128,128,128))
    draw2 = ImageDraw.Draw(img2)
    draw2.text((100,100),"testtest")
    img2.save('data/dst/pillow_imagedraw2.jpg')

image_create()

