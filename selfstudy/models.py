from django.db import models


class Chapter(models.Model):
    """Класс для описания модели Раздел."""

    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'

    def __str__(self):
        return f'{self.title}'


class Material(models.Model):
    """Класс для описания модели Материал."""

    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

    def __str__(self):
        return f'{self.title}'


class TestMaterial(models.Model):
    """Класс для описания модели Тест для Материала."""

    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='материал')
    question = models.CharField(max_length=300, verbose_name='вопрос')
    answer = models.CharField(max_length=100, verbose_name='ответ')

    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return f'{self.question}'
