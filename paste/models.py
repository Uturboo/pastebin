from django.db import models
from django.db.models import fields

# Create your models here.


class Code(models.Model):
    org_text = fields.TextField()
    md_text = fields.TextField()
    c_time = fields.DateTimeField(auto_now_add=True)
    u_time = fields.DateTimeField(auto_now=True)
