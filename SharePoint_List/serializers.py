from rest_framework import serializers

class SharePointItemSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return instance.properties