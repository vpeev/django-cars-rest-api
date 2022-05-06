from django.db import models
from django.utils import timezone

class SoftDeleteModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def delete(self, using=None, soft=True, *args, **kwargs):
        if soft:
            self.deleted_at = timezone.now()
            self.save(using=using)
        else:
            return super().delete(using=using, *args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.id is not None:
            self.update_at = timezone.now()
        super().save(*args, **kwargs)
