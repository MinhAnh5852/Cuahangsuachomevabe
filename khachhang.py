from django.db import models

class KhachHang(models.Model):
    ten_khach_hang = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    so_dien_thoai = models.CharField(max_length=15)
    dia_chi = models.TextField()

    def __str__(self):
        return self.ten_khach_hang
