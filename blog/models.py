from django.db import models
from django.db.models import CharField, DateField
from django.db.models.fields.files import ImageField
import datetime

class post(models.Model):
    title = CharField(max_length= 100)
    description = CharField(max_length= 250)
    image = ImageField (upload_to= 'blog/images/')
    date = DateField(datetime.date.today)
