from django.db import models

# Create your models here.


class quotemodeltable(models.Model):
    quote = models.TextField("My field label", null=True, blank=True)
