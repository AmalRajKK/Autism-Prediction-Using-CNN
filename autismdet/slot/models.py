from django.db import models
from doctor.models import Doctor
# Create your models here.
class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    slot_number = models.CharField(max_length=45)
    from_field = models.CharField(db_column='from', max_length=45)  # Field renamed because it was a Python reserved word.
    to = models.CharField(max_length=45)
    # dr_id = models.IntegerField()
    dr = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'slot'


