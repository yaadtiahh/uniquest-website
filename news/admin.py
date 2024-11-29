from django.contrib import admin
from .models import News
from django.utils.safestring import mark_safe


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "is_published")
    list_filter = ("created_at", "is_published")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("title", "slug", "content", "image")}),
        ("Стиль", {
            "fields": ("background_color", "text_color", "background_image"),
            "description": "Настройте внешний вид новости."
        }),
        ("Статус", {"fields": ("is_published",)}),
        ("Временная информация", {"fields": ("created_at", "updated_at")}),
    )

    def preview(self, obj):
        return mark_safe(f"""
        <div style="
            background-color: {obj.background_color};
            color: {obj.text_color};
            padding: 10px;
            margin-top: 10px;
            text-align: center;
        ">
            <h3>Пример оформления</h3>
            <p>Текст с выбранными цветами</p>
        </div>
        """)
    preview.short_description = "Предпросмотр стиля"
