from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(null=True,unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('website:category_detail', args=[str(self.slug)])


class Post(models.Model):  
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    read_time = models.IntegerField()
    slug = models.SlugField(null=True,unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    class Meta:
        ordering = ('title',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def get_absolute_url(self):
        return reverse('website:post_detail', args=[str(self.category.slug, self.slug)])

    def __str__(self):
        return self.title


