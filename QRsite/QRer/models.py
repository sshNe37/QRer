from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    email = models.EmailField(blank=True, max_length=100)

    def __str__(self):
        return str(self.title)

    class Meta:
        db_table = 'contacts'


class CustomUser(AbstractUser):
    studentname = models.CharField(max_length=100)
    first_name = None
    last_name = None

    # usernameとpasswordの指定は不要
    REQUIRED_FIELDS = ["email", "studentname"]