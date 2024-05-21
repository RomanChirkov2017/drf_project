from django.urls import path
from rest_framework import routers

from materials.apps import MaterialsConfig
from materials.views import (CourseViewSet, LessonCreateView, LessonDeleteView,
                             LessonDetailView, LessonListView,
                             LessonUpdateView, PaymentsViewSet)

app_name = MaterialsConfig.name

urlpatterns = [
    path("lessons/", LessonListView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson_detail"),
    path("lessons/<int:pk>/update/", LessonUpdateView.as_view(), name="lesson_update"),
    path("lessons/<int:pk>/delete/", LessonDeleteView.as_view(), name="lesson_delete"),
]

router = routers.SimpleRouter()
router.register("course", CourseViewSet)
router.register("payments", PaymentsViewSet)

urlpatterns += router.urls
