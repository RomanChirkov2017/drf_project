# Generated by Django 4.2 on 2024-05-23 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_alter_lesson_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
                verbose_name="Курс",
            ),
        ),
    ]
