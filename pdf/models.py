from gzip import FTEXT
from django.db import models

# Create your models here.


class Profile(models.Model):
    '''Model definition for Profile.'''

    class Meta:
        '''Meta definition for Profile.'''

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField()
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.TextField()
    skills = models.TextField()