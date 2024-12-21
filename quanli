from django.db import models

# Create your models here.
class Manager(models.Model):  
    name = models.CharField(max_length=255)  # Tên quản lý
    gender = models.BooleanField()  # Giới tính (True: Nam, False: Nữ)
    birth_day = models.DateField()  # Ngày sinh
    department = models.CharField(max_length=100)  # Phòng ban

class Course(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
