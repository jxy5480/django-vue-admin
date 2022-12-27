from django.shortcuts import render

# Create your views here.
from crud_seawater.models import CrudSeawaterModel
from crud_seawater.serializers import CrudSeawaterModelSerializer, CrudSeawaterModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet

class CrudSeawaterModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CrudSeawaterModel.objects.all()
    serializer_class = CrudSeawaterModelSerializer
    create_serializer_class = CrudSeawaterModelCreateUpdateSerializer
    update_serializer_class = CrudSeawaterModelCreateUpdateSerializer
    filter_fields = ['time', 'seawater']
    search_fields = ['time', 'seawater']