from django.db import models

class AlmondTable(models.Model):
    timestamp = models.CharField(db_column='TimeStamp', primary_key=True, max_length=50)
    deviceid = models.CharField(db_column='DEVICEID', max_length=50)  # Field name made lowercase.
    angle = models.CharField(db_column='ANGLE', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlmondTable'
        app_label = 'AlmondApp'
