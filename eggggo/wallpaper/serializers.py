from rest_framework.serializers import ModelSerializer
from .models import Wall, Classify, Notice, Banner


class ClassifySerializer(ModelSerializer):
    class Meta:
        model = Classify
        fields = "__all__"


class WallSerializer(ModelSerializer):
    class Meta:
        model = Wall
        fields = "__all__"


class NoticeSerializer(ModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
