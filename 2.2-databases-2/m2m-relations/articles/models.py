from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    slug = models.SlugField(max_length=255, unique=True, null=True, db_index=True, verbose_name='URL')
    scopes = models.ManyToManyField('Scopes', through='Tag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(* args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Scopes(models.Model):

    scope = models.CharField(max_length=50, verbose_name='Раздел')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.scope)
        super(Scopes, self).save(* args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.scope


class Tag(models.Model):

    tag = models.ForeignKey(Scopes, on_delete=models.PROTECT, related_name='tag')
    scopes = models.ForeignKey(Article, on_delete=models.PROTECT)
    is_main = models.BooleanField(u'Главная')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.tag}_{self.scopes}'
