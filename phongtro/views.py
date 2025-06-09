from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from .models import PhongTro, KhachThue, HoaDon, HopDong
from .serializers import PhongTroSerializer, KhachThueSerializer, HoaDonSerializer, HopDongSerializer

soNgayDuocTinhThanhMotThang = 7

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        
        "API PHÒNG TRỌ": "=========PHÒNG TRỌ==========",
        "Danh Sách Phòng Trọ [GET]": "api/v1/phongtro/phong-tro/",
        "Thêm Phòng Trọ [POST]": "api/v1/phongtro/phong-tro-create/",
        "Phòng Trọ Chi Tiết [GET]": "api/v1/phongtro/phong-tro/<str:pk>/",
        "Cập Nhật Phòng Trọ [POST]": "api/v1/phongtro/phong-tro-update/",
        "Xóa Phòng Trọ [DELETE]": "api/v1/phongtro/phong-tro-delete/",

        "API KHÁCH THUÊ": "=========KHÁCH THUÊ==========",
        "Danh Sách Khách Thuê [GET]": "api/v1/phongtro/khach-thue/",
        "Thêm Khách Thuê [POST]": "api/v1/phongtro/khach-thue-create/",
        "Khách Thuê Chi Tiết [GET]": "api/v1/phongtro/khach-thue/<str:pk>/",
        "Cập Nhật Khách Thuê [POST]": "api/v1/phongtro/khach-thue-update/",
        "Xóa Khách Thuê [DELETE]": "api/v1/phongtro/khach-thue-delete/",

        "API HÓA ĐƠN": "=========HÓA ĐƠN==========",
        "Danh Sách Hóa Đơn [GET]": "api/v1/phongtro/hoa-don/",
        "Thêm Hóa Đơn [POST]": "api/v1/phongtro/hoa-don-create/",
        "Hóa Đơn Chi Tiết [GET]": "api/v1/phongtro/hoa-don/<str:pk>/",
        "Cập Nhật Hóa Đơn [POST]": "api/v1/phongtro/hoa-don-update/",
        "Xóa Hóa Đơn [DELETE]": "api/v1/phongtro/hoa-don-delete/",
        "Thanh Toán Hóa Đơn [POST]": "api/v1/phongtro/thanh-toan-hoa-don/",

        "API HỢP ĐỒNG": "=========HỢP ĐỒNG==========",
        "Danh Sách Hợp Đồng [GET]": "api/v1/phongtro/hop-dong/",
        "Thêm Hợp Đồng [POST]": "api/v1/phongtro/hop-dong-create/",
        "Hợp Đồng Chi Tiết [GET]": "api/v1/phongtro/hop-dong/<str:pk>/",
        "Cập Nhật Hợp Đồng [POST]": "api/v1/phongtro/hop-dong-update/",
        "Xóa Hợp Đồng [DELETE]": "api/v1/phongtro/hop-dong-delete/",
    }
    return Response(api_urls)

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
    khach_thue_all = KhachThue.objects.all()
    serializer = KhachThueSerializer(khach_thue_all, many=True)
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
    # Lấy danh sách hợp đồng của khách thuê
    hop_dongs = HopDong.objects.filter(khachthue=khach_thue.id)
    
    thongTinChiTiet = {
        'hoten': khach_thue.hoten,
        'ngaysinh': khach_thue.ngaysinh,
        'diachi': khach_thue.diachi,
        'cccd': khach_thue.cccd,
        'dienthoai': khach_thue.dienthoai,
        'email': khach_thue.email,
        'hop_dongs': HopDongSerializer(hop_dongs, many=True).data,
    }

    return Response(thongTinChiTiet)
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

    #khách thuê id từ request
    hop_dong_id = request.data.get('hopdongid')
    hopDong = HopDong.objects.get(id=hop_dong_id)

    #ngày tạo hóa đơn
    ngayHienTai = date.today().strftime("%Y-%m-%d")
    #ngày muốn thanh toán
    #Nhập theo format YYYY-MM
    thangNam = datetime.strptime(request.data.get('hoaDonCuaThangNam'), "%Y-%m")
    # Lấy ngày đầu tháng
    hoaDonCuaThangNam = thangNam.strftime("%Y-%m-01")

    # So sánh với ngày hiện tại và ngày kết thúc hợp đồng
    # Nếu ngày tháng lớn hơn ngày hiện tại hoặc lớn hơn ngày kết thúc hợp đồng thì không cho tạo hóa đơn
    ngayKetThucHopDong = hopDong.ngayketthuc.strftime("%Y-%m-%d")
    if hoaDonCuaThangNam > ngayHienTai or hoaDonCuaThangNam > ngayKetThucHopDong:
        return Response({"error": "Ngày muốn thanh toán không hợp lệ. Vui lòng chọn ngày trong khoảng thời gian hợp đồng."})
    

    #Lay giá phòng từ hợp đồng
    phong_tro_id = hopDong.phongtro.id
    phongtro = PhongTro.objects.get(id=phong_tro_id)
    giaPhong = phongtro.giaphong

    newHoaDon = {
        'id': new_id,
        'hopdong': hopDong.id,
        'ngaytao': ngayHienTai,
        'tonghoadon': giaPhong,  # Tổng hóa đơn sẽ được tính bằng giá phòng
        'trangthai': 'Chưa thanh toán',  # Mặc định là chưa thanh toán
        'hoaDonCuaThangNam': hoaDonCuaThangNam,  # Ngày muốn thanh toán
    }
    serializer = HoaDonSerializer(data=newHoaDon)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def thanh_toan_hoa_don(request):
    hoa_don = HoaDon.objects.get(id=request.data['id'])
    # Cập nhật ngày thanh toán
    hoa_don.ngaythanhtoan = request.data.get('ngaythanhtoan', date.today().strftime("%Y-%m-%d"))
    # Cập nhật trạng thái hóa đơn
    hoa_don.trangthai = "Đã thanh toán"
    hoa_don.save()

    new_hoa_don = HoaDon.objects.get(id=request.data['id'])
    serializer = HoaDonSerializer(new_hoa_don, many=False)
    return Response(serializer.data)


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
# Hop Dong
@api_view(['GET'])
def hop_dong_list(request):
    hop_dongs = HopDong.objects.all()
    serializer = HopDongSerializer(hop_dongs, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def hop_dong_create(request):
    # Tạo ID tự động cho hợp đồng
    new_id = create_custom_id(HopDong, 'CT')
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

# Tìm thông tin khách thuê chi tiết bằng tên khách thuê
@api_view(['GET'])
def danh_sach_khach_thue_by_name(request, name):
    try:
        khach_thue = KhachThue.objects.filter(hoten__contains=name)
        serializer = KhachThueSerializer(khach_thue, many=False)
        return Response(serializer.data)
    except KhachThue.DoesNotExist:
        return Response({"error": "Khách thuê không tồn tại"})

@api_view(['GET'])
def initialize_database(request):

    # Initialize PhongTro
    PhongTro(id= 'PT000001', dientich=20, giaphong=5_500_000, loaiphong='Phòng đôi', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000002', dientich=16, giaphong=4_500_000, loaiphong='Phòng đôi', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000003', dientich=16, giaphong=4_500_000, loaiphong='Phòng đơn', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000004', dientich=20, giaphong=5_500_000, loaiphong='Phòng đôi', mota='Đầy đủ nội thất').save()
    PhongTro(id= 'PT000005', dientich=20, giaphong=5_500_000, loaiphong='Phòng đôi', mota='Đầy đủ nội thất').save()
    
    # Initialize KhachThue
    KhachThue(id='KT000001', hoten='Nguyễn Văn A', ngaysinh='1990-01-01', diachi='123 Đường ABC, Quận 1, Tp.HCM', cccd='123456789012', dienthoai='0901234567').save()
    KhachThue(id='KT000002', hoten='Trần Thị B', ngaysinh='1992-02-02', diachi='456 Đường DEF, Quận 2, Tp.HCM', cccd='987654321098', dienthoai='0912345678').save()
    KhachThue(id='KT000003', hoten='Trần Thị C', ngaysinh='1993-02-02', diachi='456 Đường XYZ, Quận 5, Tp.HCM', cccd='987654321098', dienthoai='0912345678').save()

    # Initialize HoaDon
    # HoaDon(id='HD000001', khachthue=KhachThue.objects.get(id='KT000001'), ngaytao='2023-01-01', phongtro=PhongTro.objects.get(id='PT000001'), ngaythanhtoan='2023-01-01', trangthai='Đã thanh toán', tonghoadon=5000000).save()
    # HoaDon(id='HD000002', khachthue=KhachThue.objects.get(id='KT000002'), ngaytao='2023-01-01', phongtro=PhongTro.objects.get(id='PT000002'), ngaythanhtoan='2023-01-01', trangthai='Chưa thanh toán', tonghoadon=4500000).save()

    # Initialize HopDong
    HopDong(id='CT000001', khachthue=KhachThue.objects.get(id='KT000001'), phongtro=PhongTro.objects.get(id='PT000001'), ngaybatdau='2025-01-01', ngayketthuc='2025-12-31').save()
    HopDong(id='CT000002', khachthue=KhachThue.objects.get(id='KT000002'), phongtro=PhongTro.objects.get(id='PT000002'), ngaybatdau='2025-01-01', ngayketthuc='2025-12-31').save()

    # Cap nhat lai trang thai phong tro
    phong_tro_1 = PhongTro.objects.get(id='PT000001')
    phong_tro_1.trangthai = 'Đã thuê'
    phong_tro_1.save()
    phong_tro_2 = PhongTro.objects.get(id='PT000002')
    phong_tro_2.trangthai = 'Đã thuê'
    phong_tro_2.save()
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
