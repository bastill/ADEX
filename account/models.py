from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ApprovedManager(models.Manager):
    def get_queryset(self):
        return super(ApprovedManager, self).get_queryset().filter(status=True)



class PendingManager(models.Manager):
    def get_queryset(self):
        return super(PendingManager, self).get_queryset().filter(status=False)


class UserProfile(models.Model):
    objects = models.Manager()
    pending = PendingManager()
    approved = ApprovedManager()

    user =  models.OneToOneField(User, related_name = 'userprofile')
    phone_number = models.CharField(max_length=14, blank=False)
    date_activated = models.DateTimeField(null=True)
    t_and_c = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} phone number {}".format(self.user, self.phone_number)


    class Meta:
        ordering = ('-date_activated',)


    def is_static_active(self):
        if self.status == True :
            return True

        else:
            return False
