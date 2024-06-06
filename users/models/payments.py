from django.db import models

from materials.models import Course, Lesson
from users.models.user import User

NULLABLE = {"blank": True, "null": True}


class Payments(models.Model):
    PAYMENTS_CHOICES = [
        ("cash", "Наличные"),
        ("transfer", "Перевод"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, **NULLABLE, verbose_name="Пользователь"
    )
    payment_date = models.DateTimeField(
        auto_now_add=True, **NULLABLE, verbose_name="Дата оплаты"
    )
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс"
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name="Оплаченный урок"
    )
    payment_amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(
        **NULLABLE,
        choices=PAYMENTS_CHOICES,
        verbose_name="Способ оплаты",
    )
    session_id = models.CharField(
        max_length=255, **NULLABLE, verbose_name="Id сессии"
    )
    link = models.URLField(
        max_length=450, **NULLABLE, verbose_name="Ссылка на оплату"
    )

    def __str__(self):
        return f"{self.user}: {self.payment_amount} ({self.payment_date})"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ("-payment_date",)
