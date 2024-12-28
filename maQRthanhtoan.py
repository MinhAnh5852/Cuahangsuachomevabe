import qrcode
from pyzbar import pyzbar #pyzbar doc du lieu tu ma qr
from PIL import Image #pillow xu ly hinh anh
#tao ma qr
#thong tin thanh toan
payment_info = """
Tên cửa hàng: Sữa Mẹ Và Bé
Số tài khoản: 123456789
Ngân hàng: ABC Bank
Số điện thoại: 0986543212
"""
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(payment_info)
qr.make(fit=True)

# chinh mau sac qr
img = qr.make_image(fill='black', back_color='white')
img.save("store_payment_qr_colored.png")
print("Mã QR đã được tạo và lưu với tên 'store_payment_qr_colored.png'")

# giai ma qr
# mo ma qr vua tao
img = Image.open("store_payment_qr_colored.png")

# giai ma qr
decoded_qr = pyzbar.decode(img)

# kiem tra va in
if decoded_qr:
    print("Nội dung trong mã QR:")
    print(decoded_qr[0].data.decode('utf-8'))  # lay noi dung tu ma qr
else:
    print("Không tìm thấy mã QR trong hình ảnh.")
