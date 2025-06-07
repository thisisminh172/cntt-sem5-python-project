from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview),
    path("phong-tro/", views.phong_tro_list),
    path("phong-tro-create/", views.phong_tro_create),
    path("phong-tro/<str:pk>/", views.phong_tro_detail),
    path("phong-tro-update/", views.phong_tro_update),
    path("phong-tro-delete/<str:pk>/", views.phong_tro_delete),
    path("khach-thue/", views.khach_thue_list),
    path("khach-thue-create/", views.khach_thue_create),
    path("khach-thue/<str:pk>/", views.khach_thue_detail), # Detail view of khach thue and contracts details
    path("khach-thue-update/", views.khach_thue_update),
    path("khach-thue-delete/<str:pk>/", views.khach_thue_delete),
    path("hop-dong/", views.hop_dong_list),
    path("hop-dong-create/", views.hop_dong_create),
    path("hop-dong/<str:pk>/", views.hop_dong_detail),
    path("hop-dong-update/", views.hop_dong_update),
    path("hop-dong-delete/<str:pk>/", views.hop_dong_delete),
    path("hoa-don/", views.hoa_don_list),
    path("hoa-don-create/", views.hoa_don_create),
    path("hoa-don/<str:pk>/", views.hoa_don_detail),
    path("hoa-don-update/", views.hoa_don_update),
    path("hoa-don-delete/<str:pk>/", views.hoa_don_delete),
    path("thanh-toan-hoa-don/", views.thanh_toan_hoa_don),
    # path("xuat-hoa-don/", views.xuat_hoa_don),
    # path("hoa-don-thang/", views.hoa_don_thang_list),
    path("khoitaodulieubandau/", views.initialize_database),
]
