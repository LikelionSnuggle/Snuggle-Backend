import rest_framework.serializers as serializers
from .models import Page, Page_intro, Page_notice, Page_member, Concert, Concert_location, Calender
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PageIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_intro
        fields = ('intro_detail', 'intro_link',)


class PageNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_notice
        fields = ('noti_time', 'noti_con', 'noti_img')


class PageMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page_member
        fields = ('name', 'img', 'role')


class PageDetailSerializer(serializers.ModelSerializer):
    Page_intro = PageIntroSerializer()
    Page_notice = PageNoticeSerializer(many=True)
    Page_member = PageMemberSerializer(many=True)

    class Meta:
        model = Page
        fields = ('user_seq', 'page_name',
                  'page_img', 'Page_notice', 'Page_intro', 'Page_member')


class PageListSerializer(serializers.ModelSerializer):
    Page_intro = PageIntroSerializer()
    Page_notice = PageNoticeSerializer(many=True)
    Page_member = PageMemberSerializer(many=True)

    class Meta:
        model = Page
        fields = ('page_seq', 'user_seq', 'page_name', 'page_img',
                  'Page_intro', 'Page_notice', 'Page_member')

    def create(self, validated_data):
        page_intro_data = validated_data.pop('Page_intro')
        page_notice_data = validated_data.pop('Page_notice')
        page_member_data = validated_data.pop('Page_member')

        page = Page.objects.create(**validated_data)

        Page_intro.objects.create(page_seq=page, **page_intro_data)
        for notice_data in page_notice_data:
            Page_notice.objects.create(page_seq=page, **notice_data)
        for member_data in page_member_data:
            Page_member.objects.create(page_seq=page, **member_data)

        return page


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
