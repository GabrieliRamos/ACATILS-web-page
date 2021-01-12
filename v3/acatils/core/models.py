import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone

from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


def get_file_path(_instance, filename):
    extension = filename.split('.')[-1]
    return f'{uuid.uuid4()}.{extension}'


class Base(models.Model):
    created = models.DateTimeField('Criado em:',default=timezone.now)
    modified = models.DateTimeField('Modificado em:', auto_now=True)

    class Meta:
        abstract = True


class Categories(Base):
    category = models.CharField('Categoria', max_length=100)
    description = models.TextField('Descrição', max_length=700, blank=True)
    color = models.CharField('Cor', max_length=7)
    slug = models.SlugField('Slug', blank=True, editable=False, max_length=1000)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})


class News(Base):
    title = models.CharField('Título', max_length=300)
    category = models.ForeignKey('core.Categories', verbose_name='Categoria', on_delete=models.CASCADE)
    img = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}, blank=True)
    author = models.CharField('Autor', max_length=200)
    text = models.TextField('Texto')
    slug = models.SlugField('Slug', blank=True, editable=False, max_length=1000) 

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-details', kwargs={'slug': self.slug})


def categories_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.category)

def news_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.title)

signals.pre_save.connect(categories_pre_save, sender=Categories)
signals.pre_save.connect(news_pre_save, sender=News)
