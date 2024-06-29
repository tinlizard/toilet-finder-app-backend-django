from .models import Toilet,Review
from rest_framework import serializers

class ToiletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toilet
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'