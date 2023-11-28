# 회원가입
from django.db import models

from django.contrib.auth.models import User


class UserInfo(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    birth = models.DateField()
    # password1 = models.CharField(max_length=400)
    # password2 = models.CharField(max_length=400)

    # 들어갈정보? -> 닉네임,이메일, 전화번호, 생일, 아이디, 비밀번호,
# + 회원일련번호
