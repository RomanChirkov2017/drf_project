from rest_framework.serializers import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        youtube = 'https://www.youtube.com/'
        video_link = value.get(self.field)
        if video_link and (youtube not in video_link):
            raise ValidationError("Доступны ссылки только на домен www.youtube.com")
