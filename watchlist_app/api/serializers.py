from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform,Review

class ReviewsSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields="__all__"
        
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many =True , read_only = True)
    class Meta:
        model = WatchList
        fields= "__all__"
    
    # id =serializers.IntegerField(read_only = True)
    # name = serializers.CharField()
    # description = serializers.CharField()
    # active= serializers.BooleanField()
    
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    # def create(self, validated_data):
    #     name = validated_data["name"]
    #     des = validated_data["description"]
    #     act = validated_data["active"]
        
    #     return Movie.objects.create(
    #         name =name,
    #         description = des,
    #         active =act
    #     )
        
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name" , instance.name)
    #     instance.description = validated_data.get("description" , instance.description)
    #     instance.active = validated_data.get("active" , instance.active)
    #     instance.save()
    #     return instance
    
    # def validate_title(self, value): 
    #     if len(value) < 2:
    #         raise serializers.ValidationError("short name")
    #     if self.initial_data.get("storyline") == value:
    #         raise serializers.ValidationError("name and des should not be the same")
    #     return value
    

class StreamPlatformSerializer(serializers.ModelSerializer):
    watch_list = WatchListSerializer(many = True , read_only =True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"