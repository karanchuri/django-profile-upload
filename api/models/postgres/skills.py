from django.db import models


class Skills(models.Model):
    display_name = models.CharField(max_length=25)
    constant_name = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
