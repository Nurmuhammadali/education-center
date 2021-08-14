from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from subjects.models import Subjects


class Teacher(models.Model):
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone_number = PhoneNumberField()
    address = models.TextField
    passport_seria_number = models.CharField(max_length=10)
    subjects_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

