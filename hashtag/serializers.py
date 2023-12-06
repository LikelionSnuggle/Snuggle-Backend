import rest_framework.serializers as serializers
import sys

sys.path.append("../django_back")
from django_back.models import Concert, Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = '__all__'
