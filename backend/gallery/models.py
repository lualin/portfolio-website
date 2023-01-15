from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse

# Create your models here.

# Category model
class Category(models.Model):
    title = models.CharField(null=True, blank=False, max_length=200)

    # Utility Variables
    uniqueID = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    tag = models.CharField(null=True, blank=False, max_length=50)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name_plural = ('1. Categories')

    def __str__(self):
        return '{}/{}'.format(self.title, self.uniqueID)

    def get_absolute_url(self):
        return f'/gallery/{self.tag}'

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueID is None:
            self.uniqueID = str(uuid4()).split('-')[4]
            self.slug = slugify('{}'.format(self.uniqueID))

        self.slug = slugify('{}'.format(self.uniqueID))
        self.last_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)

# Album model
class Album(models.Model):
    title = models.CharField(null=True, blank=False, max_length=200)
    description = models.TextField(null=True, blank=True)

    # Utility Variables
    uniqueID = models.CharField(null=True, blank=True, max_length=100)
    active = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    date_updated = models.DateTimeField(blank=True, null=True, auto_now=True)

    ## Related Fields
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('2. Albums')

    def __str__(self):
        return '{}/{}'.format(self.title, self.uniqueID)

    def get_absolute_url(self):
        return f'/{self.pk}'

    def save(self, *args, **kwargs):
        if self.uniqueID is None:
            self.uniqueID = str(uuid4()).split('-')[4]

        super(Album, self).save(*args, **kwargs)

# Image model
class Image(models.Model):
    title = models.CharField(null=True, blank=False, max_length=200)
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    ##ImageFields
    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='square')
    landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')
    tallImage = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg', upload_to='tall')

    ##Related Fields
    album = models.ForeignKey(Album, null=True, blank=False, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    last_updated = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        verbose_name_plural = ('3. Images')

    def __str__(self):
        return '{} {}'.format(self.album.title, self.uniqueId)


    # def get_absolute_url(self):
    #     #return reverse('image-detail', kwargs={'slug': self.slug})
    #     return f'/{self.uniqueId}/'

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.album.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)