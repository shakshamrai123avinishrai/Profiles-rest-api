from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
"""Serializers a name field for testing our APIView"""
