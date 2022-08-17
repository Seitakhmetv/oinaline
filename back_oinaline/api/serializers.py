from rest_framework import serializers
from api.models import Platform, Publisher, Genre, Type, Screenshot, Game

class PlatformSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        platform = Platform.objects.create(
            title = validated_data.get('title')
            )
        return platform
    
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()
        return instance

class PublisherSerializer(serializers.Serializer):


    id = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        publisher = Publisher.objects.create(
            title = validated_data.get('title')
            )
        return publisher
    
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()
        return instance

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        genre = Genre.objects.create(
            title = validated_data.get('title')
            )
        return genre
    
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()
        return instance

class TypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

    def create(self, validated_data):
        genre = Type.objects.create(
            title = validated_data.get('title')
            )
        return genre
    
    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.save()
        return instance

class ScreenshotSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    url = serializers.CharField()

    def create(self, validated_data):
        screenshot = Screenshot.objects.create(
            title = validated_data.get('url'),
            name = validated_data.get('name')
        )
        return screenshot
    
    def update(self, instance, validated_data):
        instance.url = validated_data['url']
        instance.name = validated_data['name']
        instance.save()
        return instance

class GameSerializer(serializers.ModelSerializer):
    platforms = PlatformSerializer(read_only=True, many=True)
    screenshots = ScreenshotSerializer(read_only=True, many=True)
    genres = GenreSerializer(read_only=True, many=True)
    publishers = PublisherSerializer(read_only=True, many=True)
    types = serializers.PrimaryKeyRelatedField(queryset=Type.objects.all())



    class Meta:
        model = Game
        fields = (
            'id', 'title', 'platforms', 'screenshots', 'trailer', 
            'genres', 'types', 'description', 'metacritic', 'publishers'
            )

