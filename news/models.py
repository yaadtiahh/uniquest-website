from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = RichTextField(help_text="Вы можете использовать HTML или стилизовать текст с разными цветами.")
    description = models.TextField(blank=True, verbose_name='Текст новости:')
    news_image = models.ImageField(upload_to='news-imgs', null=True, verbose_name='Изображение для новости')
    content_image = models.ImageField(upload_to='content_imgs', null=True, verbose_name='Фон для блока новости')
    published_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title
