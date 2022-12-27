from crud_dissolved_oxygen.models import CrudDissolvedOxygenModel
from dvadmin.utils.serializers import CustomModelSerializer


class CrudDissolvedOxygenModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = CrudDissolvedOxygenModel
        fields = "__all__"


class CrudDissolvedOxygenModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = CrudDissolvedOxygenModel
        fields = '__all__'