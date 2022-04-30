from rest_framework import serializers

class UrlSerializer(serializers.Serializer):
    actual = serializers.CharField()
    shortcode = serializers.CharField()
    last_seen_date = serializers.DateField()
    redirect_count = serializers.IntegerField()
    start_date = serializers.DateField()