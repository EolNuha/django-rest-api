from django.db import models


class NonDeleted(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_deleted=False)


class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)
    everything = models.Manager()
    objects = NonDeleted()

    def delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True
