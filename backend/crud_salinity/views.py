from django.shortcuts import render

# Create your views here.
from crud_salinity.models import CrudSalinityModel
from crud_salinity.serializers import CrudSalinityModelSerializer, CrudSalinityModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class CrudSalinityModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CrudSalinityModel.objects.all()
    serializer_class = CrudSalinityModelSerializer
    create_serializer_class = CrudSalinityModelCreateUpdateSerializer
    update_serializer_class = CrudSalinityModelCreateUpdateSerializer
    filter_fields = ['time', 'salinity']
    search_fields = ['time', 'salinity']