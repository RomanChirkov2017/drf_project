from rest_framework import serializers

from materials.models import Course, Lesson
from users.models import Payments


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'image', 'description', 'owner', 'lesson_count', 'lessons']
