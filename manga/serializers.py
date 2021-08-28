from rest_framework import serializers

from .models import *


class MangaSerializer(serializers.Serializer):
    class Meta:
        model = Manga
        fields = '__all__'


class ChapterSerializer(serializers.Serializer):
    class Meta:
        model = Chapter
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PageSerializer(serializers.Serializer):
    class Meta:
        model = PageFile
        fields = '__all__'