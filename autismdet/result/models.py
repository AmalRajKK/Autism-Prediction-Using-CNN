from django.db import models
from doctor.models import Doctor
from user.models import User
from book.models import Book
# Create your models here.


class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=250)
    result = models.CharField(max_length=45)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # book_id = models.IntegerField(blank=True, null=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'result'
