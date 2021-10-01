from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import *


class TaglineFormset(BaseInlineFormSet):
    def clean(self):
        counter_topics = 0
        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                counter_topics += 1

        if counter_topics == 0:
            raise ValidationError('Выберите основной раздел статьи')
        if counter_topics > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()


class TagInline(admin.TabularInline):
    model = Tag
    formset = TaglineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Scopes)
class ScopesAdmin(admin.ModelAdmin):
    ordering = ['tag']
    prepopulated_fields = {'slug': ('tag',)}
