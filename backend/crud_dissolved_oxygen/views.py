from django.shortcuts import render

# Create your views here.
from crud_dissolved_oxygen.models import CrudDissolvedOxygenModel
from crud_dissolved_oxygen.serializers import CrudDissolvedOxygenModelSerializer, CrudDissolvedOxygenModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class CrudDissolvedOxygenModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = CrudDissolvedOxygenModel.objects.all()
    serializer_class = CrudDissolvedOxygenModelSerializer
    create_serializer_class = CrudDissolvedOxygenModelCreateUpdateSerializer
    update_serializer_class = CrudDissolvedOxygenModelCreateUpdateSerializer
    filter_fields = ['time', 'dissolved_oxygen']
    search_fields = ['time', 'dissolved_oxygen']