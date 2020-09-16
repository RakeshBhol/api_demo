from rest_framework import serializers
from . models import Member, Period



class Period_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = ('start_time', 'end_time')


class Member_Serializer(serializers.ModelSerializer):
    tz = serializers.CharField()
    member = Period_Serializer(read_only=True, many=True)
    class Meta:
        model = Member
        fields = ('id', 'real_name', 'tz','member')
