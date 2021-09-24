from django.db import models
# from django.utils.text import slugify
from pytils.translit import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="цена")
    image = models.CharField(verbose_name="Ссылка на картинку", max_length=255, null=True, blank=True)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(* args, **kwargs)
