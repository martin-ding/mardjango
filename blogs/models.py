from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    pub_time = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.name

    def was_xiaoming(self):
        return self.name == 'xiaoming'

    was_xiaoming.admin_order_field = "tagline"
    was_xiaoming.boolean = False
    was_xiaoming.short_description = "Published recently?"

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')
    last_accessed = models.DateTimeField()

    def __str__(self):
        return  self.name

class Books(models.Model):
    name = models.CharField(max_length=50)
    pub_time = models.DateTimeField(default=timezone.now())
    price = models.FloatField()

    def __str__(self):
        return  self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

