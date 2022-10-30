from django.core.exceptions import *
from django.db import models
from django.core.validators import *


def min_length_validator(value):
    error_message = "The username must be a minimum of 2 chars"
    min_value = 2
    if len(value) < min_value:
        raise ValidationError(error_message)


def year_validation(value):
    error_message = "Year must be between 1980 and 2049"
    min_valid_year = 1980
    max_valid_year = 2049

    if min_valid_year > value or max_valid_year < value:
        raise ValidationError(error_message)


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 10
    MIN_USERNAME_LENGTH = 2
    MIN_AGE = 18
    PASSWORD_MAX_LENGTH = 30
    NAME_MAX_LENGTH = 30
    username = models.CharField(max_length=MAX_USERNAME_LENGTH, validators=[min_length_validator])
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(MIN_AGE)])
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    first_name = models.CharField(max_length=NAME_MAX_LENGTH, null=True, blank=True)
    last_name = models.CharField(max_length=NAME_MAX_LENGTH, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    MIN_PRICE = 1
    MAX_MODEL_CHAR_LENGTH = 20
    MIN_MODEL_CHAR_LENGTH = 2
    CAR_TYPE_MAX_LENGTH = 10
    CAR_TYPE_CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other"),
    )
    type = models.CharField(max_length=CAR_TYPE_MAX_LENGTH, choices=CAR_TYPE_CHOICES)
    car_model = models.CharField(max_length=MAX_MODEL_CHAR_LENGTH,
                                 validators=[MinLengthValidator(MIN_MODEL_CHAR_LENGTH)])
    year = models.IntegerField(validators=[year_validation])
    image = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(MIN_PRICE)])
