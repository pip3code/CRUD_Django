from django.db import models

# Create your models here.
class DashboardCollection(models.Model):
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.description

class DashboardPage(models.Model):
    collection = models.ForeignKey(DashboardCollection, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    
    
    def __str__(self):
        return self.description