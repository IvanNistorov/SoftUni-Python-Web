from django.db import models
from django.core.validators import *


def username_validator(value):
    error_message = "Ensure this value contains only letters, numbers, and underscore."
    if not value.isalnum() and not '_' in value:
        raise ValidationError(error_message)


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2
    MIN_AGE_VALUE = 0
    username = models.CharField(max_length=USERNAME_MAX_LENGTH,
                                validators=[MinLengthValidator(USERNAME_MIN_LENGTH), username_validator])
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)


class Album(models.Model):
    PRICE_MIN_VALUE = 0
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    GENRE_CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )
    album_name = models.CharField(max_length=ALBUM_NAME_MAX_LENGTH, unique=True)
    artist = models.CharField(max_length=ARTIST_NAME_MAX_LENGTH)
    genre = models.CharField(max_length=GENRE_MAX_LENGTH, choices=GENRE_CHOICES)
    description = models.TextField(null=True, blank=True)
    image = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(PRICE_MIN_VALUE)])
