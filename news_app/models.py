from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    description = models.TextField("Контент")
    image = models.CharField("URL изображения", max_length=500)
    post_date = models.DateTimeField("Дата и время публикации", default=datetime.now)

    def __str__(self):
        return f"{self.title}"
    