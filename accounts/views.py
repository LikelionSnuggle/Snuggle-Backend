
from django.http import JsonResponse
from .serializers import UserSerializer, UserInfoSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import viewsets
from rest_framework.views import APIView

from .models import User, UserInfo
from .serializers import UserInfoSerializer
from rest_framework.authtoken.models import Token


class signupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print("post!")
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            infoData = {}
            # infoData["username"] = 
            user = User.objects.get(username=serializer.data["username"])
            infoData["username"] = user.id
            infoData["birth"] = request.data["birth"]
            infoData["tel"] = request.data["tel"]
            infoData["email"] = serializer.data["email"]
            infoserializer = UserInfoSerializer(data=infoData)

            if infoserializer.is_valid():
                print("true")
                infoserializer.save()
                print("Userinfo created successfully")
                token = Token.objects.create(user=serializer.instance)
                return Response({"Message": "User created successfully", "token": token.key, "user_id": serializer.instance.id}, status=201)
            else:
                print("false")
                return Response(infoserializer.errors, status=400)
        else:
            return Response(serializer.errors, status=400)
        # return JsonResponse(serializer.data)
        # return Response(UserInfoSerializer.errors, status=400)

# 회원가입은 제대로 되는데, 토큰 발행이 제대로 안됨
# 글고 Username 이 회원가입 완료 시 떴으면 좋겠는데 안뜸..
#


# from django.contrib.auth import login
# from accounts.forms import SignupForm
# from django.shortcuts import render, redirect
# # from django.http import JsonResponse

# # Create your views here.


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # 회원가입 완료

#             id = form.cleaned_data.get('id')
#             username = form.cleaned_data.get('username')
#             birth = form.cleaned_data.get('birth')
#             tel = form.cleaned_data.get('tel')

#             login(request, user)  # 회원가입과 동시에 로그인
#             return redirect('/')
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html', {'form': form})

