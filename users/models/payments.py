from django.db import models

from materials.models import Course, Lesson
from users.models.user import User

NULLABLE = {"blank": True, "null": True}


class Payments(models.Model):
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
        verbose_name="Способ оплаты",
        help_text="Оплата наличными или перевод на счет?",
    )

    def __str__(self):
        return f"{self.user}: {self.payment_amount} ({self.payment_date})"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
