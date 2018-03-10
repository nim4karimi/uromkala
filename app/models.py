from django.db import models

# Main Pagee Service Model

class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    icon = models.FileField(upload_to='pic/', blank=True, null=True)

    def __str__(self):
        return self.name