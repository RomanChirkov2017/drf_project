from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

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


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now_add=True, **NULLABLE, verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='Оплаченный урок')
    payment_amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(**NULLABLE, verbose_name='Способ оплаты', help_text='Оплата наличными или перевод на счет?')

    def __str__(self):
        return f"{self.user}: {self.payment_amount} ({self.payment_date})"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
