from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import FormView
from rest_framework import viewsets


from .serializers import *


class MangaView(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer


class ChapterView(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class CommentsView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PageView(viewsets.ModelViewSet):
    queryset = PageFile.objects.all()
    serializer_class = PageSerializer

from .models import *
from .forms import *
def create_to_feed(request):
    user = request.user
    if request.method == 'POST':
        form = FeedModelForm(request.POST)
        file_form = FileModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('file') #field name in model
        if form.is_valid() and file_form.is_valid():
            feed_instance = form.save(commit=False)
            feed_instance.user = user
            feed_instance.save()
            for f in files:
                file_instance = PageFile(file=f, feed=feed_instance)
                file_instance.save()
    else:
        form = FeedModelForm()
        file_form = FileModelForm()


