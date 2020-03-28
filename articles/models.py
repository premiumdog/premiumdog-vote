from django.db import models
from gallery.models import Gallery
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

GENDER = [
    ('Kan', 'Kan'),
    ('Szuka', 'Szuka'),
]

GROUP = [
    ('Őrző- és terelőkutyák a svájci kutyák kivételével', 'Őrző- és terelőkutyák a svájci kutyák kivételével'),
    ('Pinscherek és schnauzer - molosszusok és svájci havasi kutyák', 'Pinscherek és schnauzer - molosszusok és svájci havasi kutyák'),
    ('Terrierek', 'Terrierek'),
    ('Tacskók', 'Tacskók'),
    ('Spiccek és őstípusú kutyák', 'Spiccek és őstípusú kutyák'),
    ('Kopók, vérebek és rokon fajtáik', 'Kopók, vérebek és rokon fajtáik'),
    ('Vizslák', 'Vizslák'),
    ('Spánielek, retrieverek', 'Spánielek, retrieverek'),
    ('Társasági és kísérőkutyák', 'Társasági és kísérőkutyák'),
    ('Agarak', 'Agarak'),
    ('FCI által nem elismert kutyafajták', 'FCI által nem elismert kutyafajták'),
    ('Hobby', 'Hobby'),
]


class Gdpr(models.Model):
    title= models.CharField(max_length=100)
    slug = models.SlugField()
    body = RichTextField()

    def __str__(self):
        return self.title

class Scripts(models.Model):
    name = models.CharField(max_length=100)
    shortcode = models.CharField(max_length=100, default="")
    body = models.TextField()

    def __str__(self):
        return self.name

class Join(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()

    
    def __str__(self):
        return self.title


class Article(models.Model):
    dog_number = models.CharField(max_length=10, unique=True, default="")
    title= models.CharField(max_length=100)
    slug = models.SlugField()
    gender = models.CharField(max_length=5,default="", choices=GENDER)
    group = models.CharField(max_length=100,default="", choices=GROUP)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, default="")
    owner = models.ForeignKey('Owner',on_delete=models.CASCADE, default="")
    gallery = models.ManyToManyField(Gallery)
    thumb = models.ImageField(default='default.png', blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Donation(models.Model):
    amount = models.IntegerField()
    max_amount = models.IntegerField(default=100000)
    percent = models.CharField(max_length=200, default="")


"""
    def absolute_url(self):
        return reverse("articles:article_details", args=[self.id, self.slug])
  """      


class Category(models.Model):
    name = models.CharField(max_length=254)


    def __str__(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length=254)


    def __str__(self):
        return self.name


