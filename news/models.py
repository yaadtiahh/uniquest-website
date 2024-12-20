from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.TextField(help_text="Вы можете использовать HTML или стилизовать текст с разными цветами.")
    description = RichTextField(blank=True, verbose_name='Текст новости:')
    news_image = models.ImageField(upload_to='news-imgs', null=True, verbose_name='Изображение для новости')
    content_image = models.ImageField(upload_to='content_imgs', null=True, verbose_name='Фон для блока новости')
    published_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    is_visible = models.BooleanField(default=True, verbose_name="Показывать новость")

    def __str__(self):
        return self.title
