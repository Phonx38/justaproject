from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """CUSTOM USER MODEL"""

    GENDER_CHOICES = (("male", "Male"), ("female", "Female"), ("other", "Other"))

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_HINDI = "hn"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_HINDI, "Hindi"))

    CURRENCY_USD = "usd"
    CURRENCY_RS = "rs"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_RS, "RS"))

    avatar = models.ImageField(blank=True, upload_to="avatar")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    dob = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)