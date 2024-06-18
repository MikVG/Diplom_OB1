from django.contrib import admin

from selfstudy.models import Chapter, Material, TestMaterial


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    """Регистрация в админке модели Раздел."""

    list_display = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    """Регистрация в админке модели Материал."""

    list_display = ('title', 'description', 'chapter')
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(TestMaterial)
class TestMaterialAdmin(admin.ModelAdmin):
    """Регистрация в админке модели Тест для Материала."""

    list_display = ('question', 'answer', 'material')
    list_filter = ('question',)
    search_fields = ('question',)
