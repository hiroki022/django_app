from django.db import models

# Create your models here.

class Booking(models.Model):
    lending_day = models.DateTimeField() # auto_now_addのほうが良いかもしれない
    return_day = models.DateTimeField()
    returned = models.BooleanField()

    def __str__(self):
        return self.lending_day.strftime('%Y/%m/%d')

class Camera_manage(models.Model):
    camera_name = models.CharField(max_length=100,verbose_name='カメラ名')
    camera_quantity = models.IntegerField(null=True)
    camera_number = models.IntegerField()

    def __str__(self):
        return self.camera_name

class Equipment_manage(models.Model):
    equipment_name = models.CharField(max_length=100,verbose_name='備品名')
    equipment_quantity = models.IntegerField(null=True)
    equipment_number = models.IntegerField()

    def __str__(self):
        return self.equipment_name