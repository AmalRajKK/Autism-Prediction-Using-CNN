from django.db import models

# Create your models here.
class Doctor(models.Model):
    dr_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    specilization = models.CharField(max_length=45)
    dr_address = models.CharField(max_length=45)
    dr_contactnumber = models.CharField(max_length=45)
    mailaddress = models.CharField(max_length=45)
    cirtificare = models.CharField(max_length=45)
    hospital_name = models.CharField(max_length=45)
    hospital_address = models.CharField(max_length=45)
    hospital_contact_number = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'doctor'

