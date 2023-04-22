from djongo import models

# Create your models here.
class ResonanceResult(models.Model):
    _id = models.ObjectIdField()
    task_id = models.CharField(max_length=512)
    fileName = models.CharField(max_length=255)
    fileExtension = models.CharField(max_length=20)
    completeFileName=models.CharField(max_length=255)
    predicton= models.IntegerField()    
    predicton_date= models.CharField(max_length=255)
    email= models.CharField(max_length=512)
    metadata = models.JSONField()
    
    
    class Meta:
        db_table = 'predictions_collection'

