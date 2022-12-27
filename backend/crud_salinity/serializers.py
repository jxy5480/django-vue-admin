from crud_salinity.models import CrudSalinityModel
from dvadmin.utils.serializers import CustomModelSerializer


class CrudSalinityModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = CrudSalinityModel
        fields = "__all__"


class CrudSalinityModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = CrudSalinityModel
        fields = '__all__'