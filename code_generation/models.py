from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save


class User_codes(models.Model):
    user        = models.ForeignKey(User,related_name='user_code',on_delete=models.CASCADE)
    codes       = models.CharField(max_length=17,unique=True)
    created_at  = models.DateTimeField(auto_now_add=True,auto_now=False)
    count       = models.IntegerField(default=0)
    is_used     = models.BooleanField(default=False,verbose_name='active status')


    def __str__(self):
        return self.codes

    @property
    def profile(self):
        return self.profile.all()

    class Meta:
        db_table='codes'
        ordering=['id']


class profile(models.Model):
    roles=(
        ('admin','Admin'),
        ('employee','Emp'),
        ('super','Super_user'),
    )
    pid          = models.OneToOneField(User_codes,related_name='profile',on_delete=models.CASCADE,blank=True,null=True)
    user         = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    first_name  = models.CharField(max_length=50,blank=False,null=True)
    last_name   = models.CharField(max_length=50,blank=False,null=True)
    full_name   = models.CharField(max_length=100,blank=False,null=True)
    mobile_num  = models.BigIntegerField(blank=False,null=False)
    role        = models.CharField(max_length=10,choices=roles,default='employee')
    created_at  = models.DateTimeField(auto_now_add=True,auto_now=False)
    update_at   = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.full_name


    class Meta:
        db_table='profile'



@receiver(pre_save, sender=profile)
def Create_user_full_name( instance, *args, **kwargs):
    if not instance.full_name:
        instance.full_name = instance.first_name + ' ' + instance.last_name



@receiver(post_save,sender=profile)
def status_change(instance,*args,**kwargs):
    if instance.pid:
        update=User_codes.objects.get(codes=instance.pid)
        update.is_used=True
        update.save()

