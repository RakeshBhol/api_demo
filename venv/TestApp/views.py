from django.shortcuts import render
from . models import Member, Period
from . serializers import Period_Serializer, Member_Serializer

from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class ListView(APIView):
    def get(self, request):
        query = Member.objects.all()
        serializer = Member_Serializer(query, many=True)
        return Response({"ok":"true","member": serializer.data})
