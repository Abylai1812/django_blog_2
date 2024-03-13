from rest_framework import serializers

class PostListSerializers(serializers.Serializer):
    title = serializers.CharField()
    is_active = serializers.BooleanField()
    
class PostCreateSerializer(serializers.Serializer):
    title = serializers.CharField()
    is_active = serializers.BooleanField()
    user = serializers.IntegerFieldField()
    categories = serializers.ListField()