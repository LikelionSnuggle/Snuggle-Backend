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

    def update(self, instance, validated_data):
        concert_location_data = validated_data.pop('concert_location')
        concert_location = Concert_location.objects.get(
            con_seq=instance.con_seq)
        concert_location.lat = concert_location_data.get(
            'lat', concert_location.lat)
        concert_location.lon = concert_location_data.get(
            'lon', concert_location.lon)
        concert_location.address = concert_location_data.get(
            'address', concert_location.address)
        concert_location.save()

        instance.con_name = validated_data.get('con_name', instance.con_name)
        instance.con_who = validated_data.get('con_who', instance.con_who)
        instance.con_time = validated_data.get('con_time', instance.con_time)
        instance.con_whe = validated_data.get('con_whe', instance.con_whe)
        instance.con_tag = validated_data.get('con_tag', instance.con_tag)
        instance.con_pay = validated_data.get('con_pay', instance.con_pay)
        instance.con_sum_img = validated_data.get(
            'con_sum_img', instance.con_sum_img)
        instance.user_seq = validated_data.get('user_seq', instance.user_seq)
        instance.save()
        return instance


class ConcertListSerializer(serializers.ModelSerializer):
    concert_location = ConcertLocationSerializer()

    class Meta:
        model = Concert
        fields = ('con_name', 'con_who', 'con_time', 'con_whe', 'con_tag',
                  'con_pay', 'con_sum_img', 'user_seq', 'concert_location')

    def create(self, validated_data):
        concert_location_data = validated_data.pop('concert_location')
        concert_location = Concert_location.objects.create(
            **concert_location_data)
        concert = Concert.objects.create(
            concert_location=concert_location, **validated_data)
        return concert


class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'
