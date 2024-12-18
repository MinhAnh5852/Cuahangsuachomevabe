import qrcode
my_text = "Sua cho me va be"
qr = qrcode.QRCode(version=1,box_size=10,border=10)
qr.add_data(my_text)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('mycode.png')

from pyzbar import pyzbar
from PIL import Image
img = Image.open('mycode.png')
qr_out = pyzbar.decode(img)
print(qr_out[0][0])