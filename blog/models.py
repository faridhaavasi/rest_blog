from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post_Manager(models.Manager):
    def True_status(self):
        return self.filter(status=True)


class Post(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='Post')
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, blank=True, null=True)
    created = models.DateField(auto_now_add=timezone.now)
    body = models.TextField()
    status = models.BooleanField(default=True)
    objects = Post_Manager()


    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Post, self).save()
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_as = models.DateField()


    def __str__(self):
        return self.text[:30]






