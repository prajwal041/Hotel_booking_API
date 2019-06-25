from rest_framework import serializers

from .models import Solution, Clicks

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'

class ClicksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clicks
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = "__all__"

class ClicksSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Clicks
        fields = "__all__"