from django.db import models

class Articles(models.Model):
      title = models.CharField('Название', max_length=50, default='Новость дня')
      announcement = models.CharField('Анонс', max_length=250, default='Анонс дня')
      text = models.TextField('Статья')
      date = models.DateTimeField('Дата и время публикации')

      def __str__(self):
            return self.title
      
      class Meta:
            verbose_name = 'Новость'
            verbose_name_plural = 'Новости'