from django.db import models
from .helper.government_set import GOVERNMENT_CHOICES


class Person(models.Model):

    # Gender Choices
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female')
    ]

    # Fields
    nationalID = models.BigIntegerField(
        null=False, blank=False, unique=True)
    birth_date = models.DateTimeField()
    government = models.CharField(max_length=2, choices=GOVERNMENT_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    century = models.CharField(max_length=100)

    # Represents the class objects as a string
    def __str__(self) -> str:
        return str(self.nationalID)
