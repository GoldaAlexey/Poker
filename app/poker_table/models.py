from django.db import models

class Table(models.Model):
    TableId = models.AutoField(primary_key=True)
    TableName = models.CharField(max_length=500)
    PlayerIn = models.BigIntegerField()