from django.db import models

# Create your models here.
class disease_url(models.Model):
    disease_name=models.CharField(max_length=200)
    url=models.URLField()
    def __str__(self) -> str:
        return str(self.disease_name)+' url'