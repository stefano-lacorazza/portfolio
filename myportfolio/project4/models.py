from django.db import models

class QR(models.Model):
    cover = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.cover