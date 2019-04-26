from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import studentsSerializer


class studntList(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer = studentsSerializer(students, many=True)
        return Response({"students": serializer.data})

    def post(self):
        pass
