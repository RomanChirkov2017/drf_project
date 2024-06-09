import datetime
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import pytz
from materials.models import Course, Subscription
from users.models.user import User


@shared_task
def course_update_send_mail(pk: int, date: datetime.datetime):
    instance = Course.objects.filter(id=pk).first()
    if instance:
        hour_delta = (instance.last_update - date).total_seconds() / 3600
        if hour_delta > 4:
            subs = Subscription.objects.filter(course=instance)
            if len(list(subs)) > 0:
                subscribers = []
                for sub in subs:
                    subscribers.append(User.objects.get(id=sub.user.id).email)
                send_mail(
                    subject=f"Курс {instance.name} обновлен",
                    message=f"Курс {instance.name} из Ваших подписок обновлен",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=subscribers,
                    fail_silently=False,
                )


@shared_task
def check_login():
    users = User.objects.filter(is_active=True)
    if users.exists():
        for user in users:
            if datetime.datetime.now(
                pytz.timezone("UTC")
            ) - user.last_login > datetime.timedelta(weeks=4):
                user.is_active = False
                user.save()
