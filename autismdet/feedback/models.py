from django.db import models
from doctor.models import Doctor
from result.models import Result
from user.models import User
from book.models import Book
# Create your models here.


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    # dr_id = models.IntegerField(blank=True, null=True)
    dr=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    # user_id = models.IntegerField(blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=45, blank=True, null=True)
    result = models.CharField(max_length=45, blank=True, null=True)
    image = models.CharField(max_length=45, blank=True, null=True)
    # book_id = models.IntegerField(blank=True, null=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'feedback'


class Autistic(models.Model):
    aut_is = models.AutoField(primary_key=True)
    image = models.CharField(max_length=45)
    result = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'autistic'


class Notautistic(models.Model):
    notaut_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=45)
    result = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'notautistic'

