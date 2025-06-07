from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from .models import ChiPhi, PhongTro, KhachThue, HoaDon, SinhHoat, HopDong
from .serializers import ChiPhiSerializer, PhongTroSerializer, KhachThueSerializer, HoaDonSerializer, SinhHoatSerializer, HopDongSerializer

soNgayDuocTinhThanhMotThang = 7

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "API CHI PHÍ": "=========CHI PHÍ==========",
        "Danh sách Chi Phí [GET]": "/chi-phi/",
        "Thêm Chi Phí [POST]": "/chi-phi-create/",
        "Chi Phí Chi Tiết [GET]": "/chi-phi/<str:pk>/",
        "Cập Nhật Chi Phí [POST]": "/chi-phi-update/",
        "Xóa Chi Phí [DELETE]": "/chi-phi-delete/",
        
        "API PHÒNG TRỌ": "=========PHÒNG TRỌ==========",
        "Danh Sách Phòng Trọ [GET]": "/phong-tro/",
        "Thêm Phòng Trọ [POST]": "/phong-tro-create/",
        "Phòng Trọ Chi Tiết [GET]": "/phong-tro/<str:pk>/",
        "Cập Nhật Phòng Trọ [POST]": "/phong-tro-update/",
        "Xóa Phòng Trọ [DELETE]": "/phong-tro-delete/",

        "API KHÁCH THUÊ": "=========KHÁCH THUÊ==========",
        "Danh Sách Khách Thuê [GET]": "/khach-thue/",
        "Thêm Khách Thuê [POST]": "/khach-thue-create/",
        "Khách Thuê Chi Tiết [GET]": "/khach-thue/<str:pk>/",
        "Cập Nhật Khách Thuê [POST]": "/khach-thue-update/",
        "Xóa Khách Thuê [DELETE]": "/khach-thue-delete/",

        "API HÓA ĐƠN": "=========HÓA ĐƠN==========",
        "Danh Sách Hóa Đơn [GET]": "/hoa-don/",
        "Thêm Hóa Đơn [POST]": "/hoa-don-create/",
        "Hóa Đơn Chi Tiết [GET]": "/hoa-don/<str:pk>/",
        "Cập Nhật Hóa Đơn [POST]": "/hoa-don-update/",
        "Xóa Hóa Đơn [DELETE]": "/hoa-don-delete/",

        "API SINH HOẠT": "=========SINH HOẠT==========",
        "Danh Sách Sinh Hoạt [GET]": "/sinh-hoat/",
        "Thêm Sinh Hoạt [POST]": "/sinh-hoat-create/",
        "Sinh Hoạt Chi Tiết [GET]": "/sinh-hoat/<str:pk>/",
        "Cập Nhật Sinh Hoạt [POST]": "/sinh-hoat-update/",
        "Xóa Sinh Hoạt [DELETE]": "/sinh-hoat-delete/",

        "API HỢP ĐỒNG": "=========HỢP ĐỒNG==========",
        "Danh Sách Hợp Đồng [GET]": "/hop-dong/",
        "Thêm Hợp Đồng [POST]": "/hop-dong-create/",
        "Hợp Đồng Chi Tiết [GET]": "/hop-dong/<str:pk>/",
        "Cập Nhật Hợp Đồng [POST]": "/hop-dong-update/",
        "Xóa Hợp Đồng [DELETE]": "/hop-dong-delete/",
    }
    return Response(api_urls)

# Chi Phi
@api_view(['GET'])
def chi_phi_list(request):
    chi_phis = ChiPhi.objects.all()
    serializer = ChiPhiSerializer(chi_phis, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def chi_phi_create(request):
    # Tạo ID tự động cho chi phí
    new_id = create_custom_id(ChiPhi, 'CP')
    request.data['id'] = new_id
    serializer = ChiPhiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['GET'])
def chi_phi_detail(request, pk):
    chi_phi = ChiPhi.objects.get(id=pk)
    serializer = ChiPhiSerializer(chi_phi, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def chi_phi_update(request):
    chi_phi = ChiPhi.objects.get(id=request.data['id'])
    serializer = ChiPhiSerializer(instance=chi_phi, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def chi_phi_delete(request, pk):
    chi_phi = ChiPhi.objects.get(id=pk)
    chi_phi.delete()
    return Response("Đã xóa thành công chi phí")
# Phong Tro
@api_view(['GET'])
def phong_tro_list(request):
    phong_tros = PhongTro.objects.all()
    serializer = PhongTroSerializer(phong_tros, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def phong_tro_create(request):
    # Tạo ID tự động cho phòng trọ
    new_id = create_custom_id(PhongTro, 'PT')
    request.data['id'] = new_id
    serializer = PhongTroSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['GET'])
def phong_tro_detail(request, pk):
    phong_tro = PhongTro.objects.get(id=pk)
    serializer = PhongTroSerializer(phong_tro, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def phong_tro_update(request):
    phong_tro = PhongTro.objects.get(id=request.data['id'])
    serializer = PhongTroSerializer(instance=phong_tro, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def phong_tro_delete(request, pk):
    phong_tro = PhongTro.objects.get(id=pk)
    phong_tro.delete()
    return Response("Đã xóa thành công phòng trọ")
# Khach Thue
@api_view(['GET'])
def khach_thue_list(request):
    khach_thues = KhachThue.objects.all()
    serializer = KhachThueSerializer(khach_thues, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def khach_thue_create(request):
    # Tạo ID tự động cho khách thuê
    new_id = create_custom_id(KhachThue, 'KT')
    request.data['id'] = new_id
    serializer = KhachThueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['GET'])
def khach_thue_detail(request, pk):
    khach_thue = KhachThue.objects.get(id=pk)
    serializer = KhachThueSerializer(khach_thue, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def khach_thue_update(request):
    khach_thue = KhachThue.objects.get(id=request.data['id'])
    serializer = KhachThueSerializer(instance=khach_thue, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def khach_thue_delete(request, pk):
    khach_thue = KhachThue.objects.get(id=pk)
    khach_thue.delete()
    return Response("Đã xóa thành công khách thuê")
# Hoa Don
@api_view(['GET'])
def hoa_don_list(request):
    hoa_dons = HoaDon.objects.all()
    serializer = HoaDonSerializer(hoa_dons, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def hoa_don_create(request):
    # Tạo ID tự động cho hóa đơn
    new_id = create_custom_id(HoaDon, 'HD')
    request.data['id'] = new_id
    serializer = HoaDonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['GET'])
def hoa_don_detail(request, pk):
    hoa_don = HoaDon.objects.get(id=pk)
    serializer = HoaDonSerializer(hoa_don, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def hoa_don_update(request):
    hoa_don = HoaDon.objects.get(id=request.data['id'])
    serializer = HoaDonSerializer(instance=hoa_don, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def hoa_don_delete(request, pk):
    hoa_don = HoaDon.objects.get(id=pk)
    hoa_don.delete()
    return Response("Đã xóa thành công hóa đơn")
# Sinh Hoat
@api_view(['GET'])
def sinh_hoat_list(request):
    sinhhoats = SinhHoat.objects.all()
    serializer = SinhHoatSerializer(sinhhoats, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def sinh_hoat_create(request):
    # Tạo ID tự động cho sinh hoạt
    new_id = create_custom_id(SinhHoat, 'SH')
    request.data['id'] = new_id
    serializer = SinhHoatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['GET'])
def sinh_hoat_detail(request, pk):
    sinhhoat = SinhHoat.objects.get(id=pk)
    serializer = SinhHoatSerializer(sinhhoat, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def sinh_hoat_update(request):
    sinhhoat = SinhHoat.objects.get(id=request.data['id'])
    serializer = SinhHoatSerializer(instance=sinhhoat, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def sinh_hoat_delete(request, pk):
    sinhhoat = SinhHoat.objects.get(id=pk)
    sinhhoat.delete()
    return Response("Đã xóa thành công sinh hoạt")
# Hop Dong
@api_view(['GET'])
def hop_dong_list(request):
    hop_dongs = HopDong.objects.all()
    serializer = HopDongSerializer(hop_dongs, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def hop_dong_create(request):
    # Tạo ID tự động cho hợp đồng
    new_id = create_custom_id(HopDong, 'HD')
    request.data['id'] = new_id
    serializer = HopDongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['GET'])
def hop_dong_detail(request, pk):
    hop_dong = HopDong.objects.get(id=pk)
    serializer = HopDongSerializer(hop_dong, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def hop_dong_update(request):
    hop_dong = HopDong.objects.get(id=request.data['id'])
    serializer = HopDongSerializer(instance=hop_dong, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
@api_view(['DELETE'])
def hop_dong_delete(request, pk):
    hop_dong = HopDong.objects.get(id=pk)
    hop_dong.delete()
    return Response("Đã xóa thành công hợp đồng")

@api_view(['POST'])
def tinh_hoa_don(request):
    # Tính hóa đơn của tháng hiện tại
    tonghoadon = 0
    soThang = 1
    ngayHoaDon = ''

    khachthue_id = request.data['khachthue_id']
    phongtro_id = request.data['phongtro_id']

    khachthue = KhachThue.objects.get(id=khachthue_id)
    phongtro = PhongTro.objects.get(id=phongtro_id)

    giaDien = ChiPhi.objects.get(ten='dien').gia # lay 1 gia tri
    giaNuoc = ChiPhi.objects.get(ten='nuoc').gia # lay 1 gia tri
    giaInternet = ChiPhi.objects.get(ten='internet').gia # lay 1 gia tri
    giaGiatDo = ChiPhi.objects.get(ten='giatdo').gia # lay 1 gia tri
    giaRac = ChiPhi.objects.get(ten='rac').gia

    giaPhong = PhongTro.objects.get(id=phongtro_id).giaphong

    sinhhoat = SinhHoat.objects.get(khachthue=khachthue, phongtro=phongtro)
    # lay so sinh hoat
    soDien = sinhhoat.dien
    soNuoc = sinhhoat.nuoc


    hopdong = HopDong.objects.get(khachthue=khachthue, phongtro=phongtro)
    # lay so thang datetime.strptime(date_string, format)
    ngayBatDau = datetime.strptime(str(hopdong.ngaybatdau), "%Y-%m-%d").date()
    ngayHienTai = datetime.now().date()

    # thangNgayHienTai = ngayHienTai.strftime("%m-%d")

    ngayNgayBatDau = ngayBatDau.day
    ngayNgayHienTai = ngayHienTai.day

    if ngayNgayHienTai > ngayNgayBatDau and ngayNgayHienTai - ngayNgayBatDau > soNgayDuocTinhThanhMotThang: 
        ngayHoaDon = ngayHienTai.strftime("%Y-%m-%d")
    else:
        ngayHoaDon = (ngayHienTai - relativedelta(months=1)).strftime("%Y-%m-%d")

    
    tienDienPhaiTra = soDien * giaDien
    tienNuocPhaiTra = soNuoc * giaNuoc
    tienInternetPhaiTra = giaInternet * soThang
    tienGiatDoPhaiTra = giaGiatDo * soThang
    tienRacPhaiTra = giaRac * soThang
    tienPhongPhaiTra = giaPhong * soThang
    # Tính tổng hóa đơn
    tonghoadon = tienDienPhaiTra + tienNuocPhaiTra + tienInternetPhaiTra + tienGiatDoPhaiTra + tienRacPhaiTra + tienPhongPhaiTra
    
    return Response({
        'khachthue': khachthue.hoten,
        'phongtro': phongtro.sophong,
        'ngayHoaDon': ngayHoaDon,
        'tienDienPhaiTra': tienDienPhaiTra,
        'tienNuocPhaiTra': tienNuocPhaiTra,
        'tienInternetPhaiTra': tienInternetPhaiTra,
        'tienGiatDoPhaiTra': tienGiatDoPhaiTra,
        'tienRacPhaiTra': tienRacPhaiTra,
        'tienPhongPhaiTra': tienPhongPhaiTra,
        'tonghoadon': tonghoadon,
    })

@api_view(['GET'])
def initialize_database(request):
    # Initialize ChiPhi
    
    ChiPhi(id= 'CP000001', ten='dien', gia=3000, donvi='kilowat').save()
    ChiPhi(id= 'CP000002', ten='nuoc', gia=2000, donvi='khối').save()
    ChiPhi(id= 'CP000003', ten='internet', gia=100000, donvi='tháng').save()
    ChiPhi(id= 'CP000004', ten='giatdo', gia=120000, donvi='tháng').save()
    ChiPhi(id= 'CP000005', ten='rac', gia=15000, donvi='tháng').save()

    # Initialize PhongTro
    PhongTro(id= 'PT000001', sophong='1', diachi='123/4 Đường Trần Xuân Soạn, Quận 7, Tp.HCM', dientich=20, giaphong=5_500_000, loaiphong='Phòng đôi', trangthai='Đã thuê', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000002', sophong='2', diachi='123/4 Đường Trần Xuân Soạn, Quận 7, Tp.HCM', dientich=16, giaphong=4_500_000, loaiphong='Phòng đơn', trangthai='Đã thuê', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000003', sophong='3', diachi='123/4 Đường Trần Xuân Soạn, Quận 7, Tp.HCM', dientich=16, giaphong=4_500_000, loaiphong='Phòng đơn', trangthai='Trống', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000004', sophong='4', diachi='123/4 Đường Trần Xuân Soạn, Quận 7, Tp.HCM', dientich=20, giaphong=5_500_000, loaiphong='Phòng đôi', trangthai='Đã thuê', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000005', sophong='5', diachi='123/4 Đường Trần Xuân Soạn, Quận 7, Tp.HCM', dientich=20, giaphong=5_500_000, loaiphong='Phòng đôi', trangthai='Trống', mota='Đầy đủ nội thất').save()
    
    # Initialize KhachThue
    KhachThue(id='KT000001', hoten='Nguyễn Văn A', ngaysinh='1990-01-01', diachi='123 Đường ABC, Quận 1, Tp.HCM', cccd='123456789012', dienthoai='0901234567').save()
    KhachThue(id='KT000002', hoten='Trần Thị B', ngaysinh='1992-02-02', diachi='456 Đường DEF, Quận 2, Tp.HCM', cccd='987654321098', dienthoai='0912345678').save()

    # Initialize HoaDon
    HoaDon(id='HD000001', khachthue=KhachThue.objects.get(id='KT000001'), ngaytao='2023-01-01', phongtro=PhongTro.objects.get(id='PT000001'), ngaythanhtoan='2023-01-01', trangthai='Đã thanh toán', tonghoadon=5000000).save()
    HoaDon(id='HD000002', khachthue=KhachThue.objects.get(id='KT000002'), ngaytao='2023-01-01', phongtro=PhongTro.objects.get(id='PT000002'), ngaythanhtoan='2023-01-01', trangthai='Chưa thanh toán', tonghoadon=4500000).save()

    # Initialize SinhHoat
    SinhHoat(id='SH000001', khachthue=KhachThue.objects.get(id='KT000001'), phongtro=PhongTro.objects.get(id='PT000001'), dien=100, nuoc=10).save()
    SinhHoat(id='SH000002', khachthue=KhachThue.objects.get(id='KT000002'), phongtro=PhongTro.objects.get(id='PT000002'), dien=150, nuoc=15).save()

    # Initialize HopDong
    HopDong(id='HD000001', khachthue=KhachThue.objects.get(id='KT000001'), phongtro=PhongTro.objects.get(id='PT000001'), ngaybatdau='2023-01-01', ngayketthuc='2024-01-01', tiencoc=11_000_000).save()
    HopDong(id='HD000002', khachthue=KhachThue.objects.get(id='KT000002'), phongtro=PhongTro.objects.get(id='PT000002'), ngaybatdau='2023-01-01', ngayketthuc='2024-01-01', tiencoc=9_000_000).save()

    return Response({
        'message': 'Database initialized successfully'
    })

def create_custom_id(model, prefix):
    last_record = model.objects.order_by('id').last()
    if last_record:
        last_id = last_record.id
        new_id = prefix + str(int(last_id[2:]) + 1).zfill(6)
        
    else:
        new_id = prefix + '000001'
    return new_id
