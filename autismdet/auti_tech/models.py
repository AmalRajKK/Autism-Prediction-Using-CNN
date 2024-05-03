from django.db import models

# Create your models here.
class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=45)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'image'
