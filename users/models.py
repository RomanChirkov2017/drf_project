from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Укажите почту"
    )

    first_name = models.CharField(max_length=150, verbose_name="Имя", **NULLABLE)
    last_name = models.CharField(max_length=200, verbose_name="Фамилия", **NULLABLE)
    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Укажите телефон",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )
    city = models.CharField(
        max_length=150, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
