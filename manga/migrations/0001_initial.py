from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import manga.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65, unique=True)),
                ('description', models.TextField()),
                ('rating', models.SmallIntegerField(default=0, validators=[manga.models.validate_rating])),
                ('image', models.ImageField(blank=True, null=True, upload_to='manga_covers')),
                ('author', models.CharField(max_length=65)),
                ('artist', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='PageFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='manga_pages')),
                ('Which_Chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='manga.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='manga.chapter')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.manga'),
        ),
    ]
