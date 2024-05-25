# Generated by Django 4.2 on 2024-05-25 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_alter_lesson_course"),
        ("users", "0004_alter_payments_paid_course_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="paid_course",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
                verbose_name="Оплаченный курс",
            ),
            preserve_default=False,
        ),
    ]
