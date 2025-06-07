# serializers.py
from rest_framework import serializers
from .models import PhongTro, KhachThue, HoaDon, HopDong

class PhongTroSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhongTro
        fields = '__all__'
class KhachThueSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhachThue
        fields = '__all__'
class HoaDonSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoaDon
        fields = '__all__'

class HopDongSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopDong
        fields = '__all__'
