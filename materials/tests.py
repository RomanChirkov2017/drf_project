from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Course, Lesson
from users.models.user import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@mail.com',
            password='12345'
        )
        self.course = Course.objects.create(
            title='test_course',
            description='test_description',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            title='test_lesson',
            video_link='https://www.youtube.com/',
            course=self.course,
            owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        """ Тестирование создания уроков. """

        data = {
            "title": self.lesson.title,
            "video_link": self.lesson.video_link,
            "course": self.lesson.course.id,
            "owner": self.lesson.owner.id
        }

        response = self.client.post(
            '/materials/lessons/create/', data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_lesson_list(self):
        """ Тестирование вывода списка уроков. """

        response = self.client.get(
            '/materials/lessons/',
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_retrieve(self):
        """ Тестированиие вывода одного урока. """

        data = {
            "title": self.lesson.title,
            "video_link": self.lesson.video_link,
            "course": self.lesson.course.id,
            "owner": self.lesson.owner.id
        }

        response = self.client.get(
            f'/materials/lessons/{self.lesson.id}/', data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_update(self):
        """ Тестирование на обновление урока. """

        data = {
            "title": "updated_test_lesson",
            "video_link": self.lesson.video_link,
            "course": self.lesson.course.id,
            "owner": self.lesson.owner.id
        }

        response = self.client.patch(
            f'/materials/lessons/{self.lesson.id}/update/', data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        """ Тестирование удаления урока. """

        data = {
            "title": "delete test",
            "description": "delete test"
        }

        response = self.client.delete(
            f'/materials/lessons/{self.lesson.id}/delete/', data=data
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@mail.com',
            password='12345'
        )
        self.course = Course.objects.create(
            title='test_course',
            description='test_description',
            owner=self.user
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_view(self):
        """ Тестирование подписки на обновления. """

        data = {
            "user": self.user.id,
            "course": self.course.id
        }

        response = self.client.post(
            '/materials/subscription/', data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json(), {'message': 'Подписка добавлена'})
