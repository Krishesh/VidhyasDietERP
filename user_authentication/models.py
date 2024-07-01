from django.contrib.auth.models import User
from django.db import models

from humanresource.models import Employee
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, blank=True, null=True)
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Dietitian', 'Dietitian'),
        ('Therapist', 'Therapist'),
        ('Guest', 'Guest'),
        ('', 'default'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='default')

    def __str__(self):
        return '%s' % (self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
