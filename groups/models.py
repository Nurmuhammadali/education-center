from django.db import models

# Create your models here.
from subjects.models import Subjects
from teachers.models import Teacher
from user.models import User


class Groups(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, default=None)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE, blank=True, default=None)
    def __str__(self):
        return self.name



class GroupSubject(models.Model):
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE,  default=None)
    student_id = models.ForeignKey(User, on_delete=models.CASCADE,  default=None)
    created_student_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_id.name


