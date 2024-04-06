from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    cimage=models.ImageField(upload_to='categoryimages',blank=True)


    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('websiteapp:movies_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Movies(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    poster=models.ImageField(upload_to='movies',blank=True)
    release_date=models.DateField()
    actors=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    trailer=models.URLField(max_length=250)

    def get_url(self):
        return reverse('websiteapp:MovieCatDetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.name)


class  review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Movies, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=100)
    rating = models.IntegerField()


