from django.conf import settings
from django.db import models

from users.models.user import User

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=250, verbose_name="Название", help_text="Введите название"
    )
    image = models.ImageField(
        upload_to="materials/",
        verbose_name="Превью",
        help_text="Загрузите изображение",
        **NULLABLE,
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание", help_text="Введите описание"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(
        max_length=250, verbose_name="Название", help_text="Введите название"
    )
    description = models.TextField(
        **NULLABLE, verbose_name="Описание", help_text="Ведите описание"
    )
    image = models.ImageField(
        upload_to="materials/",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE,
    )
    video_link = models.CharField(
        max_length=350,
        verbose_name="Ссылка на видео",
        **NULLABLE,
        help_text="Укажите ссылку",
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
