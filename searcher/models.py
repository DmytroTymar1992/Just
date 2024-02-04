from django.db import models
from main.models import User

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')

    def __str__(self):
        return f'Resume for {self.user.get_full_name()}'

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def phone(self):
        return self.user.phone

    @property
    def date_of_birth(self):
        return self.user.date_of_birth