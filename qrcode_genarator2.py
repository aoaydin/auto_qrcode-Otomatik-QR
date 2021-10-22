import os
os.system
from PIL import Image, ImageDraw, ImageFont
import qrcode
print("Dosya Adını Giriniz=")
name=input()
os.mkdir(name)
os.chdir(name)
print("Kaç Adet Qr Oluşturacaksın ?")
num=int(input())
for i in range(num):
    print("Oluşturulacak QRCODE Girin")
    data=input()
    pic=qrcode.make(data)
    pic.save("{0}-{1}.png".format(name,i+1))
    img = Image.open("{0}-{1}.png".format(name,i+1))
    d1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype("arial.ttf", 20 , encoding="unic")
    d1.text((25, 255), data+"  "+data , font=myFont)
    img.save("{0}-{1}.png".format(name,i+1))