from django.db import models


# Create your models here.
class ChiPhi(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    ten = models.CharField(max_length=100)
    loai = models.CharField(max_length=100,null=True, blank=True)
    donvi = models.CharField(max_length=50)
    gia = models.DecimalField(max_digits=10, decimal_places=2)
    mota = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ten
    

class PhongTro(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    sophong = models.CharField(max_length=100)
    diachi = models.CharField(max_length=200,null=True, blank=True)
    mota = models.TextField(null=True, blank=True)
    dientich = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    giaphong = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    loaiphong = models.CharField(max_length=50,null=True, blank=True) # e.g., "Phòng đơn", "Phòng đôi"
    trangthai = models.CharField(max_length=50,null=True, blank=True) # e.g., "Trống", "Đã thuê"

    def __str__(self):
        return f"{self.sophong} - {self.diachi}"
    
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
    id = models.CharField(max_length=100, primary_key=True)
    khachthue = models.ForeignKey(KhachThue, on_delete=models.CASCADE) # ForeignKey to khachthue
    phongtro = models.ForeignKey(PhongTro, on_delete=models.CASCADE) # ForeignKey to phongtro
    ngaythanhtoan = models.DateField(null=True, blank=True) # Ngày thanh toán
    trangthai = models.CharField(max_length=50) # e.g., "Đã thanh toán", "Chưa thanh toán"
    tonghoadon = models.DecimalField(max_digits=10, decimal_places=2) # Tổng hóa đơn
    ngaytao = models.DateField(auto_now_add=True) # Ngày tạo hóa đơn

    def __str__(self):
        return f"HoaDon {self.id} - {self.khachthue.hoten} - {self.phongtro.sophong} - {self.tonghoadon} VND - {self.trangthai}"
    

class SinhHoat(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    khachthue = models.ForeignKey(KhachThue, on_delete=models.CASCADE) # ForeignKey to khachthue
    phongtro = models.ForeignKey(PhongTro, on_delete=models.CASCADE) # ForeignKey to phongtro
    dien = models.DecimalField(max_digits=10, decimal_places=2) # Số điện tiêu thụ
    nuoc = models.DecimalField(max_digits=10, decimal_places=2) # Số nước tiêu thụ

    def __str__(self):
        return f"Sinh hoạt {self.id} - {self.khachthue.hoten} - {self.dien} kw - {self.nuoc} m3"
    
class HopDong(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    khachthue = models.ForeignKey(KhachThue, on_delete=models.CASCADE) # ForeignKey to khachthue
    phongtro = models.ForeignKey(PhongTro, on_delete=models.CASCADE) # ForeignKey to phongtro
    ngaybatdau = models.DateField() # Ngày bắt đầu hợp đồng
    ngayketthuc = models.DateField() # Ngày kết thúc hợp đồng
    tiencoc = models.DecimalField(max_digits=10, decimal_places=2) # tiền cọc


    def __str__(self):
        return f"Hợp đồng {self.id} - {self.khachthue.hoten} - {self.phongtro.sophong} - {self.ngaybatdau} - {self.ngayketthuc}"



    
