import rest_framework.serializers as serializers
from .models import User, Page, Page_intro, Page_notice, Concert, Concert_location, Calender


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class PageIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_intro
        fields = '__all__'


class PageNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_notice
        fields = '__all__'


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = '__all__'


class ConcertLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert_location
        fields = '__all__'


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'
