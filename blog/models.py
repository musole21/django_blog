from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

lorem_text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Error, dignissimos recusandae enim deserunt repellendus voluptatibus molestiae accusantium vitae velit! Labore fugiat cumque voluptas voluptatum numquam! Quisquam inventore animi dolorem adipisci!'


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(default=lorem_text)
    pub_date = models.DateTimeField(
        'When the post was published', default=timezone.now)
    date_modified = models.DateTimeField('Last Updated', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.first_name.capitalize()}"
