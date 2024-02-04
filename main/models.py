from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):

    class Role(models.TextChoices):
        JOB_SEEKER = 'JS', 'Пошуковець'
        EMPLOYER = 'EM', 'Роботодавець'

   
    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.JOB_SEEKER,
        verbose_name="Роль"
    )
    first_name = models.CharField(max_length=50, verbose_name="Ім'я", blank=True)
    last_name = models.CharField(max_length=50, verbose_name="Прізвище", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Номер телефону", blank=True)
    date_of_birth = models.DateField( blank=True, verbose_name="Дата народження")
    avatar = models.ImageField(upload_to='avatars/')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f' {self.first_name}, {self.last_name}, {self.role}'