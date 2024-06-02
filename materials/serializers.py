from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LinkValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, required=False)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, instance):
        request = self.context.get('request')
        user = None
        if request:
            user = request.user
        return instance.subscription_set.filter(user=user).exists()

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "image",
            "description",
            "owner",
            "lesson_count",
            "lessons",
            "subscription",
        ]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
