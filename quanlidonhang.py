from django.db import models

# Bảng sản phẩm
class Product(models.Model):
    name = models.CharField(max_length=255)  # Tên sản phẩm
    description = models.TextField()  # Mô tả
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá
    quantity = models.IntegerField()  # Số lượng
    image = models.ImageField(upload_to='products/')  # Hình ảnh
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # Danh mục

# Bảng danh mục sản phẩm
class Category(models.Model):
    name = models.CharField(max_length=255)  # Tên danh mục

# Bảng khách hàng
class Customer(models.Model):
    name = models.CharField(max_length=255)  # Tên khách hàng
    email = models.EmailField(unique=True)  # Email
    phone_number = models.CharField(max_length=15)  # Số điện thoại
    address = models.TextField()  # Địa chỉ

# Bảng đơn hàng
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Liên kết khách hàng
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Tổng tiền
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ])  # Trạng thái đơn hàng

# Bảng chi tiết đơn hàng
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Liên kết đơn hàng
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Liên kết sản phẩm
    quantity = models.IntegerField()  # Số lượng sản phẩm
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá sản phẩm

