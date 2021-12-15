from django.db import models

# Create your models here.

class Sample(models.Model):
        Minimumreal = models.FloatField(null=True)
        Minimumimag = models.FloatField(null=True)
        Maximumreal = models.FloatField(null=True)
        Maximumimag = models.FloatField(null=True)
        MaxInteration = models.IntegerField(null=True)
        xaxis = models.IntegerField(null=True)
        yaxis = models.IntegerField(null=True)

        def __float__(self):
            return self.Minimumreal    
    
