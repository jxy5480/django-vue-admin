
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.translation import gettext_lazy as _

from dvadmin.system.models import Users

from django.views.decorators.csrf import csrf_exempt

# from . import models
from django.http import JsonResponse
# Create your views here.

# @csrf_exempt 
# def PortalLoginView(request):
# 	username = request.POST.get("username")
# 	password = request.POST.get("password")
# 	print(username)
# 	print(password)

# 	return JsonResponse({'request': username})



class PortalLoginSerializer(TokenObtainPairSerializer):
    """
    登录的序列化器:
    重写djangorestframework-simplejwt的序列化器
    """

    class Meta:
        model = Users
        fields = "__all__"
        read_only_fields = ["id"]

    default_error_messages = {"no_active_account": _("Wrong username or password")}

    def validate(self, attrs):
        data = super().validate(attrs)
        data["name"] = self.user.name
        data["userId"] = self.user.id
        data["avatar"] = self.user.avatar
        request = self.context.get("request")
        request.user = self.user
        # 记录登录日志
        # save_login_log(request=request)

        # print(self.user.role.all())
        for r in self.user.role.all():
            print(r.name)

        return {"code": 2000, "msg": "Success", "data": data}


class PortalLoginView(TokenObtainPairView):
    """
    登录接口
    """

    serializer_class = PortalLoginSerializer
    permission_classes = []

class PortalDataView(TokenObtainPairView):
    serializer_class = PortalLoginSerializer
    permission_classes = []
