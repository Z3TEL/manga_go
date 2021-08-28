from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()
# RATING_CHOC

class Manga(models.Model):
    title = models.CharField(max_length=65, unique=True)
    description = models.TextField()
    rating = models.SmallIntegerField(default=1)
    image = models.ImageField(upload_to='manga_covers', blank=True, null=True)
    author = models.CharField(max_length=65)
    artist = models.CharField(max_length=65)







class Chapter(models.Model):
    manga=models.ForeignKey(Manga, on_delete=models.CASCADE)
    text=models.TextField(blank=False, max_length=100)

class PageFile(models.Model):
    file = models.FileField(upload_to="files/%Y/%m/%d")
    feed = models.ForeignKey(Chapter, on_delete=models.CASCADE)


class Comment(models.Model):
    chapter = models.ForeignKey(Chapter,
                                on_delete=models.CASCADE,
                                related_name='comment')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='comment')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

