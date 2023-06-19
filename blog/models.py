from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


# Create your models here.
class Post_Manager(models.Manager):
    def True_status(self):
        return self.filter(status=True)


class Post(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, blank=True, null=True)
    created = models.DateField(auto_now_add=timezone.now)
    body = models.TextField()
    status = models.BooleanField(default=True)
    Manager = Post_Manager()

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Post, self).save()
    def __str__(self):
        return self.title



