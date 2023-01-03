from django.db import models
from django.utils.text import slugify
from hello.validators import title_val
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255,
        validators=[title_val])
    body = models.TextField()
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.title)