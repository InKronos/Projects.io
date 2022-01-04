from rest_framework import serializers
from users.models import Projects,RatingProject

class ProjectAuthorizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        
class ProjectUnAuthorizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("pk","title", "averageRate", "stage", "description")        
class RatingProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingProject
        fields = "__all__"

