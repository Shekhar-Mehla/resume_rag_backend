from rest_framework import serializers




class ResumeSerializer(serializers.Serializer):
    input = serializers.CharField(max_length=100)
    