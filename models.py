'''
Here we create an extensible model, the purpose of this model is to add permissions fields for django-permission to all models.

'''
from django.db import models
from django.contrib.auth.models import User,Group

class RestEasy(models.Model):
    
    # These fields are used by django-permission AuthorPermissionLogic, CollaboratorsPermissionLogic, and AudiencePermission
    owner         = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_owner") # CRUD
    group 		  = models.ForeignKey(Group,related_name="%(app_label)s_%(class)s_related_group")
    collaborators = models.ManyToManyField(User,related_name="%(app_label)s_%(class)s_related_collaborators") # RU
    audience      = models.ManyToManyField(User,related_name="%(app_label)s_%(class)s_related_audience") # R
        
    class Meta:
        abstract = True
    
    def __init__(self, *args, **kwargs):
        super(RestEasy, self).__init__(*args, **kwargs)
