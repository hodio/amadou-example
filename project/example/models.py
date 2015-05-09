from django.db import models
from django.contrib.auth.models import User,Group
from rest_permissions.models import RestPermissions
from django.conf import settings

# Date Utils
from dateutil.relativedelta import *
from datetime import *
import datetime as dt

# Object Level History
from simple_history.models import HistoricalRecords
'''
This is the base class, it extends the Amadou model with the intent of adding model revision. 
It also returns a default unicode definition of object.name or object.pk
'''
class Base(RestPermissions):
     
    class Meta:
        abstract = True
        
    # Let's be conventional and provide a default unicode return of name, or in absence of the primary key
    def __unicode__(self):
        try:
            self.name
            return u'%s' % self.name
        except:
            return u'%s' % self.pk
    
class HistoryMixin(object):

    # For Simple History django-admin Hooks 
    # !!! WE MAY NEED TO CHECK IF HISTORY IS ENABLED, IF NOT DONT IMPLEMENT
    #if self.owner:
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value 

    @property
    def history_url(self):
        try: 
            self.history
        except:
            return False 
        else:
            # !!! NOTE :  Need to provide sensible default if not set
            return "%shistorical%s/%s/" % (settings.REST_BASE_URL,self.__class__.__name__.lower(),self.pk)

class Person(Base,HistoryMixin):
    
    # This must be enabled on a per model basis
    history       = HistoricalRecords()
    
    """Person model."""
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name      = models.CharField(blank=True, max_length=100)
    middle_name     = models.CharField(blank=True, max_length=100)
    last_name       = models.CharField(blank=True, max_length=100)
    slug            = models.SlugField(unique=True)
    user            = models.ForeignKey(User, blank=True, null=True, help_text='If the person is an existing user of your site.')
    gender          = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, null=True)
    avatar          = models.FileField(upload_to='avatars', blank=True)
    birth_date      = models.DateField(blank=True, null=True)
    email           = models.EmailField(null=True)
    website         = models.URLField(blank=True)

    class Meta:
        verbose_name ='person'
        verbose_name_plural = 'people'
        ordering = ('last_name', 'first_name')

    def __unicode__(self):
        return u'%s' % self.full_name

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    @property
    def age(self):
        TODAY = dt.date.today()
        return u'%s' % relativedelta(TODAY, self.birth_date).years
    
class Bicycle(Base,HistoryMixin):
    history         = HistoricalRecords()
    name            = models.CharField(max_length=100)
    front_wheel     = models.ForeignKey('Wheel',related_name="%(app_label)s_%(class)s_related_wheel_front")
    back_wheel      = models.ForeignKey('Wheel',related_name="%(app_label)s_%(class)s_related_wheel_back")
    frame           = models.ForeignKey('Frame')

class Frame(Base):
    MATERIALS       = (('Steel','Steel'),('Titanium','Titatnium'),('Aluminum','Alumninum'),('Carbon Fiber','Carbon Fiber'))
    material        = models.CharField(choices=MATERIALS, max_length=100)
    paint           = models.BooleanField(default=False)


class Wheel(Base):
    SIZES           = (('26','26 in'),('29','29 in'),('700','700cm'),)
    BRANDS          = (('Mavic','Mavic'),('Shimano','Shimano'),('Power Tap','Power Tap'))
    size            = models.CharField(choices=SIZES, max_length=100)
    brand           = models.CharField(choices=BRANDS, max_length=100)
    tire            = models.ForeignKey('Tire')

class Tire(Base):
    SIZES           = (('23cm','23cm'),('24cm','24cm'),('1in','1in'),)
    BRANDS          = (('Contintental','Continental'),('Michelin','Michelin'),('Bontrager','Bontrager'))
    brand           = models.CharField(choices=BRANDS, max_length=100)

class Scratch(Base):
    name            = models.CharField(max_length=100)
    content         = models.TextField(blank=True)
    priority        = models.PositiveSmallIntegerField()