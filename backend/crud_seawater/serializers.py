from crud_seawater.models import CrudSeawaterModel
from dvadmin.utils.serializers import CustomModelSerializer


class CrudSeawaterModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = CrudSeawaterModel
        fields = "__all__"


class CrudSeawaterModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = CrudSeawaterModel
        fields = '__all__'