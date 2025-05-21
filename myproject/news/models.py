from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    anons = models.CharField(max_length=300, verbose_name="Анонс")
    full_text = models.TextField(verbose_name="Текст статьи")
    date = models.DateField(verbose_name="Дата публикации")

    def __str__(self):
        return self.title