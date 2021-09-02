from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models


User = get_user_model()
# RATING_CHOC

def validate_rating(rating):
    if rating < 0:
        raise ValidationError(('Рейтинг не может быть ниже 0'),params={'rating': rating},)
    elif rating > 5:
        raise ValidationError(('Рейтинг не может быть выше 5'),params={'rating': rating},)
    else:
        return rating




class Manga(models.Model):
    Genre_Choices = (
        ('Horror', 'Ужастик'),
        ('Comedy', 'Комедия'),
        ('Triller', 'Триллер'),
        ('Senen', 'Сёнен'),
        ('Sedze', 'Сёдзе'),
        ('Seinen', 'Сейнен'),
    )
    title = models.CharField(max_length=65, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='manga_covers', blank=True, null=True)
    author = models.CharField(max_length=65)
    artist = models.CharField(max_length=65)
    genre = models.CharField(max_length=60, choices=Genre_Choices)

    def str(self):
        return self.title




class Chapter(models.Model):
    manga=models.ForeignKey(Manga, on_delete=models.CASCADE)
    text=models.TextField(blank=False, max_length=100)


class PageFile(models.Model):
    file = models.FileField(upload_to="manga_pages")
    Which_Chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='image')



class Comment(models.Model):
    chapter = models.ForeignKey(Chapter,
                                on_delete=models.CASCADE,
                                related_name='comment')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class BookMark(models.Model):
    Going = (
        ('All', 'Все'),
        ('Reading', 'Читаю'),
        ('In the plans', 'В планах'),
        ('Readed', 'Прочитано'),
        ('Favorites', 'Любимые'),
        ('End', 'Закончил')
    )
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='Who_is')
    add_to_favorites = models.CharField(max_length=40, choices=Going)


class Rating(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='rating_manga')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='author')
    rating = models.SmallIntegerField(default=0, validators=[validate_rating])

