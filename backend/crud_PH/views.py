from django.shortcuts import render

# Create your views here.
from crud_PH.models import CrudPHModel
from crud_PH.serializers import CrudPHModelSerializer, CrudPHModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class CrudPHModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CrudPHModel.objects.all()
    serializer_class = CrudPHModelSerializer
    create_serializer_class = CrudPHModelCreateUpdateSerializer
    update_serializer_class = CrudPHModelCreateUpdateSerializer
    filter_fields = ['time', 'ph']
    search_fields = ['time', 'ph']