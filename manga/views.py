from django_filters import rest_framework as rest_filters, NumberFilter, CharFilter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response

from .serializers import *
from django_filters import rest_framework as filters
from .permissions import *


class MangaFilter(filters.FilterSet):
    class Meta:
        model = Manga
        fields = ('genre', )

from rest_framework import filters


class MangaView(viewsets.ModelViewSet):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializer
    filter_backends = [rest_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = MangaFilter
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return MangaSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'like']:
            return [IsAdminUser()]
        elif self.action in ['like']:
            return [IsAuthenticated()]
        return []
        return []

    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        manga = self.get_object()
        user = request.user
        like_obj, created = Like.objects.get_or_create(manga=manga, user=user)
        if like_obj.is_liked:
            like_obj.is_liked = False
            like_obj.save()
            return Response('disliked')
        else:
            like_obj.is_liked = True
            like_obj.save()
            return Response('liked')


class ChapterView(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'likes']:
            return [IsAdminUser()]
        return []




class CommentsView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser(), IsAuthorOrIsAdmin()]
        return []





class PageView(viewsets.ModelViewSet):
    queryset = PageFile.objects.all()
    serializer_class = PageSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return []




from .forms import *
def create_to_pages(request):
    user = request.user
    if request.method == 'POST':
        form = FeedModelForm(request.POST)
        file_form = FileModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
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






class BookMarkViewSet(viewsets.ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthorOrIsAdmin(), IsAuthenticated()]
        return []

class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthorOrIsAdmin(), IsAuthenticated()]
        return []


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
