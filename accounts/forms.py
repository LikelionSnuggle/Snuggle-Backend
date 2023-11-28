from django import forms
from django.contrib.auth.forms import UserCreationForm


from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import User

# 원래 UserCreationForm 상속 받았는데, 여기에서 JWT 활용해서 회원가입하는걸로 바꿨습니다~!
# class SignupForm(UserCreationForm):
#     email = forms.EmailField()

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['username'].required = True
#     #     self.fields['email'].required = True
#     #     self.fields['tel'].required = True
#     #     self.fields['birth'].required = True
#     #     self.fields['id'].required = True
#     #     self.fields['password1'].required = True
#     #     self.fields['password2'].required = True

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email', 'tel', 'birth', 'id',
#                   'password1', 'password2')

# 들어갈정보? -> 전화번호, 생일, 아이디, 비밀번호, 이메일, 닉네임
# + 회원일련번호
