from crud_PH.models import CrudPHModel
from dvadmin.utils.serializers import CustomModelSerializer

class CrudPHModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = CrudPHModel
        fields = "__all__"

class CrudPHModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = CrudPHModel
        fields = '__all__'