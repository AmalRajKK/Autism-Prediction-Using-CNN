from django.db import models
from slot.models import  Slot
from user.models import  User
# Create your models here.
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    # slot_id = models.IntegerField()
    slot=models.ForeignKey(Slot,on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    date = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'book'

