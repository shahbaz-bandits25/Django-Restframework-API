from rest_framework import serializers


class studentsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    fname = serializers.CharField(max_length=10)
    year = serializers.IntegerField()
