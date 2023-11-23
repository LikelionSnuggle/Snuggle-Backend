from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from django import request
# from main import models, serializers
# from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView

from .models import User, Performance, Page, PageInfo, PageNotification, PerformanceList, Calender
from .serializers import UserSerializer, PerformanceSerializer, PageSerializer, PageInfoSerializer, PageNotificationSerializer, PerformanceListSerializer, CalenderSerializer

# from django.views.generic.edit import FormView
# from search.forms import PostSearchForm
# from django.db.models import Q
# from django.shortcuts import render 
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    
class PageInfoViewSet(viewsets.ModelViewSet):
    queryset = PageInfo.objects.all()
    serializer_class = PageInfoSerializer

class PageNotificationViewSet(viewsets.ModelViewSet):
    queryset = PageNotification.objects.all()
    serializer_class = PageNotificationSerializer

class PerformanceListViewSet(viewsets.ModelViewSet):
    queryset = PerformanceList.objects.all()
    serializer_class = PerformanceListSerializer

class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    
    
# def Search(request, searchword):
#     Performances = Performance.objects.all().filter(
#             Q(name__icontains=searchword) | #이름 검색
#             Q(content=searchword) #내용 검색
#         )
#     serializer = PerformanceSerializer(Performances, many=True)
    
#     return Response(serializer.data)

# def temp(reqeust):
    
#     if 'kw' in request.GET:
#         query = request.GET.get('kw')
#         performances = Performance.objects.all().filter(
#             Q(name__icontains=query) | #이름 검색
#             Q(content__icontains=query) #내용 검색
#         )
    
#     return render(request, 'search.html', {'query':query, 'performances':performances})

# class SearchFormView(FormView):
#     form_class = PostSearchForm
#     template_name = 'search/post_search.html'
#     post_list =Post.object.filter(Q)
 
# class SearchPerformanceViewSet(viewsets.ModelViewSet):
#     queryset = models.Book.objects.all()
#     serializer_class = serializers.BookSerializer
#     filter_backends = [DjangoFilterBackend] # DjangoFilterBackend 로 필터링 백엔드 등록
#     filterset_fields = ['title', 'author']
#     ordering_fields = ['title']

# def search(request):
#         if request.method == 'POST':
#                 searched = request.POST['searched']        
#                 recipes = Recipe.objects.filter(name__contains=searched)
#                 return render(request, 'searched.html', {'searched': searched, 'recipes': recipes})
#         else:
#                 return render(request, 'searched.html', {})


# from django.shortcuts import render
# # from store.models import Product
# from django.db.models import Q

# # filter 함수의 Q함수: OR조건으로 데이터를 조회하기 위해 사용하는 함수
# # objects.filter() 는 특정 조건에 해당하면 객체 출력 .get('kw') 은 kw만 반환
# # __icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사. 사용법 "필드명"__icontains = 조건값

# # def searchResult(request):
    
# #     if 'kw' in request.GET:
# #         query = request.GET.get('kw')
# #         products = Product.objects.all().filter(
# #             Q(name__icontains=query) | #이름 검색
# #             Q(description__icontains=query) #설명 검색
# #         )

# #     return render(request, 'search.html', {'query':query, 'products':products})