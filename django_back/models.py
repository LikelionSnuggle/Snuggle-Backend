from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

from django.contrib.auth.models import User


# class User(models.Model):  # 사용자
#     user_seq = models.AutoField(primary_key=True)

#     user_pho = models.CharField(max_length=20, validators=[RegexValidator(
#         r'^\d{2,3}-\d{3,4}-\d{4}$')])  # 정규표현식으로 전화번호 형식 지정
#     user_bth = models.DateField()  # 날짜로 받아야함
#     user_id = models.CharField(max_length=50)
#     user_pw = models.CharField(max_length=50)
#     user_email = models.EmailField(max_length=50)
#     us_name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.us_name

class Hashtag(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Page(models.Model):  # 페이지
    page_seq = models.AutoField(primary_key=True)

    # Page와 1대다로 연결
    # User의 user_seq를 foreign key로 연결
    user_seq = models.ForeignKey(User, on_delete=models.CASCADE)

    page_name = models.CharField(max_length=100)
    # page_int = models.CharField(max_length=500, null=True, blank=True)
    # page_not = models.CharField(max_length=500, null=True, blank=True)
    page_img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.page_name

    class Meta:
        ordering = ['-page_seq']  # 최신순으로 정렬


class Page_member(models.Model):  # 페이지 멤버
    # Page와 1대다로 연결
    # Page의 page_seq를 foreign key로 연결
    page_seq = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name='Page_member')
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    role = models.CharField(max_length=20)


class Page_intro(models.Model):  # 페이지 소개
    # Page와 1대1로 연결
    page_seq = models.OneToOneField(
        Page, on_delete=models.CASCADE, primary_key=True, related_name='Page_intro')

    intro_detail = models.CharField(max_length=500, null=True, blank=True)
    intro_link = models.CharField(max_length=500, null=True, blank=True)
    # intro_man = models.CharField(max_length=500, null=True, blank=True)


class Page_notice(models.Model):  # 페이지 공지
    # Page와 1대다로 연결
    # Page의 page_seq를 foreign key로 연결
    page_seq = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name='Page_notice')

    # 모델 생성시간
    noti_time = models.DateField(auto_now_add=True)
    noti_con = models.CharField(max_length=500)
    noti_img = models.ImageField(upload_to='images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.noti_time:
            self.noti_time = timezone.now().date()
        return super().save(*args, **kwargs)


class Concert_location(models.Model):  # 공연 위치

    lat = models.FloatField()
    lon = models.FloatField()
    address = models.CharField(max_length=100)

    # TODO: 가까운 정보 추가


class Concert(models.Model):  # 공연
    con_seq = models.AutoField(primary_key=True)
    # User의 user_seq를 foreign key로 연결
    user_seq = models.ForeignKey(User, on_delete=models.CASCADE)

    # Concert_location와 1대1로 연결
    concert_location = models.OneToOneField(
        Concert_location, on_delete=models.CASCADE, related_name='concert', null=True, blank=True)

    con_name = models.CharField(max_length=100)
    con_who = models.CharField(max_length=100)
    con_time = models.DateField()
    con_whe = models.CharField(max_length=100)
    con_tag = models.ManyToManyField(Hashtag, blank=True)
    con_link = models.CharField(max_length=100, null=True, blank=True)
    con_detail = models.CharField(max_length=500)
    PAY_CHOICES = [
        ('유료', '유료'),
        ('무료', '무료'),
    ]
    con_pay = models.CharField(max_length=10, choices=PAY_CHOICES)
    con_sum_img = models.ImageField(upload_to='images/', null=True, blank=True)
    con_numb = models.CharField(max_length=20, validators=[RegexValidator(
        r'^\d{2,3}-\d{3,4}-\d{4}$')])  # 정규표현식으로 전화번호 형식 지정

    def __str__(self):
        return self.con_name


class Calender(models.Model):
    page_seq = models.OneToOneField(Page, on_delete=models.CASCADE)
    con_seq = models.OneToOneField(Concert, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
