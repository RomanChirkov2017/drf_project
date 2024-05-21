from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import PaymentsViewSet

app_name = UsersConfig.name

urlpatterns = []

router = routers.SimpleRouter()
router.register("payments", PaymentsViewSet)

urlpatterns += router.urls
