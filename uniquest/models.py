from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL")
    content = RichTextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="news_images/", blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    # Новые поля для стилизации
    background_color = models.CharField(
        max_length=7,
        default="#ffffff",
        verbose_name="Цвет фона",
        help_text="Введите цвет в формате HEX, например, #ffffff."
    )
    text_color = models.CharField(
        max_length=7,
        default="#000000",
        verbose_name="Цвет текста",
        help_text="Введите цвет в формате HEX, например, #000000."
    )
    background_image = models.ImageField(
        upload_to="news_backgrounds/",
        blank=True,
        null=True,
        verbose_name="Фоновое изображение",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("news_detail", args=[self.slug])

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title