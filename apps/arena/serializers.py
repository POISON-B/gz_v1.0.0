

from rest_framework import serializers

from apps.user_relationship.models import UserAchievement
from .models import *


class TotalRankSerializers(serializers.ModelSerializer):
    """
    总排行榜序列化
    """
    class Meta:
        model = UserAchievement
        fields = "__all__"


class WeekRankSerializers(serializers.ModelSerializer):
    """
    周排行榜序列化
    """
    class Meta:
        model = UserAchievement
        fields = "__all__"


class ClassRankSerializers(serializers.ModelSerializer):
    """
    日排行榜序列化
    """
    class Meta:
        model = UserAchievement
        fields = "__all__"


class PassSerializer(serializers.ModelSerializer):
    """
    关卡信息序列化
    """
    class Meta:
        model = Pass
        fields = "__all__"


class UserPassSerializer(serializers.ModelSerializer):
    """
    用户关卡信息序列化
    """
    class Meta:
        model = UserPass
        fields = "__all__"


class ChallengerSerializer(serializers.ModelSerializer):
    """
    挑战者信息序列化
    """
    class Meta:
        model = Challenger
        fields = "__all__"


class PkDetailSerializers(serializers.ModelSerializer):
    """
    挑战者信息序列化
    """
    class Meta:
        model = UserPkDetail
        fields = "__all__"



class TeamCompSerializers(serializers.ModelSerializer):
    """
    挑战者信息序列化
    """
    class Meta:
        model = TeamComp
        fields = "__all__"

