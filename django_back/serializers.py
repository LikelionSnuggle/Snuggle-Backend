import rest_framework.serializers as serializers
from .models import User, Page, Page_intro, Page_notice, Concert, Concert_location, Calender


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PageIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_intro
        fields = ('intro_detail', 'intro_link', 'intro_man')


class PageNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_notice
        fields = ('noti_time', 'noti_con', 'noti_img')


class PageDetailSerializer(serializers.ModelSerializer):
    page_intro = PageIntroSerializer()
    page_notice = PageNoticeSerializer(many=True)

    class Meta:
        model = Page
        fields = ('user_seq', 'page_name', 'page_int', 'page_not',
                  'page_img', 'page_notice', 'page_intro')


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class ConcertLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert_location
        fields = '__all__'


class ConcertDetailSerializer(serializers.ModelSerializer):
    concert_location = ConcertLocationSerializer()

    class Meta:
        model = Concert
        fields = '__all__'


class ConcertListSerializer(serializers.ModelSerializer):
    concert_location = ConcertLocationSerializer()

    class Meta:
        model = Concert
        fields = ('con_name', 'con_who', 'con_time', 'con_whe', 'con_tag',
                  'con_pay', 'con_sum_img', 'user_seq', 'concert_location')


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'
