from rest_framework import serializers

class HelloSerializer(serializers.Serializer): #they are similar to Django forms
    """Serializes a name field for testing out an APIView post calls"""
    name = serializers.CharField(max_length=10)
