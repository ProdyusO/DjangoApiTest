from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150, required=True)
    country = serializers.CharField(max_length=100, required=False, allow_null=True, allow_blank=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()

        return instance

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150, required=True)
    genre = serializers.CharField(max_length=150, required=False, allow_null=True, allow_blank=True)
    pages = serializers.IntegerField(max_value=50, required=False)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.save()

        return instance

    def create(self, validated_data):
        return Book.objects.create(**validated_data)