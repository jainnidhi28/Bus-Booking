from django.db import models
from .mixins import AbstractTrack
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class User(AbstractUser, AbstractTrack):
    
    phone_number = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField(
        _("email address"),
        unique=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

