from django.core.validators import *
from django.db import models
from django.core import validators


class Profile(models.Model):
    MAX_PASSWORD_LENGTH = 30
    MAX_NAME_LENGTH = 30
    UPLOAD_TO_URL = 'pictures'
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(12)])
    password = models.CharField(max_length=MAX_PASSWORD_LENGTH)
    first_name = models.CharField(max_length=MAX_NAME_LENGTH, null=True, blank=True)
    last_name = models.CharField(max_length=MAX_NAME_LENGTH, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'



class Game(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 15
    UPLOAD_TO_URL = 'image'
    MIN_RATING = 0.1
    MAX_RATING = 5
    MIN_MAX_LEVEL = 1
    CATEGORY_CHOICES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=MAX_TITLE_LENGTH, unique=True)
    category = models.CharField(max_length=MAX_CATEGORY_LENGTH, choices=CATEGORY_CHOICES)
    rating = models.FloatField(validators=[MinValueValidator(MIN_RATING), MaxValueValidator(MAX_RATING)])
    max_level = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(MIN_MAX_LEVEL)])
    image = models.URLField()
    summary = models.TextField(null=True, blank=True)
