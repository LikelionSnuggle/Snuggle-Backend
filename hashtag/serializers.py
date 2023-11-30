import rest_framework.serializers as serializers
import sys

sys.path.append("../django_back")
from django_back import models


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hashtag
        fields = '__all__'
