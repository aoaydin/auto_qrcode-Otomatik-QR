import os
os.system("pip install pillow qrcode")
from PIL import Image,ImageDraw
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
