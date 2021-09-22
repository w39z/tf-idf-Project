from django.db import models

# Create your models here.
from django.db import models

from .validators import validate_file_extension


class Post(models.Model):
    upload = models.FileField(upload_to='texts/', validators=[validate_file_extension])
