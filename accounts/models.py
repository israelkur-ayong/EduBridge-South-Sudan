from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    country = models.CharField(
        max_length=100,
        blank=True
    )

    university = models.CharField(
        max_length=150,
        blank=True
    )

    course = models.CharField(
        max_length=150,
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    linkedin = models.URLField(
        blank=True
    )

    github = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.user.username