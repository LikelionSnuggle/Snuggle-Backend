import rest_framework.serializers as serializers
from .models import User, Performance, Page, PageInfo, PageNotification, PerformanceList, Calender

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class PageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageInfo
        fields = '__all__'

class PageNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageNotification
        fields = '__all__'

class PerformanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceList
        fields = '__all__'

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'