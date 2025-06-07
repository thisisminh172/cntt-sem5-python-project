from django.db import models


# Create your models here.

class PhongTro(models.Model):
    TRANGTHAI_CHOICES = [
        ('Trống', 'Trống'),
        ('Đã thuê', 'Đã thuê'),
    ]
    PHONG_CHOICES = [
        ('Phòng đơn', 'Phòng đơn'),
        ('Phòng đôi', 'Phòng đôi'),
    ]
    id = models.CharField(max_length=100, primary_key=True)
    diachi = models.CharField(max_length=200,null=True, blank=True)
    mota = models.CharField(max_length=200,null=True, blank=True)
    dientich = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    giaphong = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    loaiphong = models.CharField(max_length=10, choices=PHONG_CHOICES, default='Phòng đôi') # e.g., "Phòng đơn", "Phòng đôi"
    trangthai = models.CharField(max_length=7, choices=TRANGTHAI_CHOICES, default='Trống') # e.g., "Trống", "Đã thuê"

    def __str__(self):
        return f"{self.id} - {self.diachi}"
    
class KhachThue(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    hoten = models.CharField(max_length=100)
    ngaysinh = models.DateField()
    diachi = models.CharField(max_length=200)
    cccd = models.CharField(max_length=100)
    dienthoai = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    # PhongTro = models.ForeignKey(PhongTro, on_delete=models.CASCADE)

    def __str__(self):
        return self.hoten
    
class HoaDon(models.Model):
    TRANGTHAI_CHOICES = [
        ('Đã thanh toán', 'Đã thanh toán'),
        ('Chưa thanh toán', 'Chưa thanh toán'),
    ]
    id = models.CharField(max_length=100, primary_key=True)
    khachthue = models.ForeignKey(KhachThue, on_delete=models.CASCADE) # ForeignKey to khachthue
    phongtro = models.ForeignKey(PhongTro, on_delete=models.CASCADE) # ForeignKey to phongtro
    ngaythanhtoan = models.DateField(null=True, blank=True) # Ngày thanh toán
    trangthai = models.CharField(max_length=50, choices=TRANGTHAI_CHOICES, default='Chưa thanh toán') # e.g., "Đã thanh toán", "Chưa thanh toán"
    tonghoadon = models.DecimalField(max_digits=10, decimal_places=2) # Tổng hóa đơn
    ngaytao = models.DateField(auto_now_add=True) # Ngày tạo hóa đơn
    hoaDonCuaThangNam = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"HoaDon {self.id} - {self.khachthue.hoten} - {self.phongtro.id} - {self.tonghoadon} VND - {self.trangthai}"
    
    
class HopDong(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    khachthue = models.ForeignKey(KhachThue, on_delete=models.CASCADE) # ForeignKey to khachthue
    phongtro = models.ForeignKey(PhongTro, on_delete=models.CASCADE) # ForeignKey to phongtro
    ngaybatdau = models.DateField() # Ngày bắt đầu hợp đồng
    ngayketthuc = models.DateField() # Ngày kết thúc hợp đồng

    def __str__(self):
        return f"Hợp đồng {self.id} - {self.khachthue.hoten} - {self.phongtro.id} - {self.ngaybatdau} - {self.ngayketthuc}"



    
