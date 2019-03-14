from django.db import models
from django.utils import timezone


class ApprovedManager(models.Manager):
    def get_queryset(self):
        return super(ApprovedManager, self).get_queryset().filter(status=True)



class PendingManager(models.Manager):
    def get_queryset(self):
        return super(PendingManager, self).get_queryset().filter(status=False)




class UserActivation(models.Model):
    objects = models.Manager()
    pending = PendingManager()
    approve = ApprovedManager()

    username    =  models.CharField(max_length=50, blank=False, unique=True)
    email       =  models.EmailField(max_length=50, blank=False, unique=True)
    phone_num   =  models.CharField(max_length=13, blank=False, unique=True)
    t_and_c     =  models.BooleanField(default=False)
    password    =  models.CharField(max_length=30)
    password_2  =  models.CharField(max_length=30)
    date_created = models.DateTimeField(timezone.now())
    status     =   models.BooleanField(default=False)


    def __str__(self):
        return "{} and {}".format(self.username, self.email)


    class Meta:
        ordering = ('-date_created',)
