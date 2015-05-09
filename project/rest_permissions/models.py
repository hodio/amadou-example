'''
Here we create an extensible model, the purpose of this model is to add permissions fields for django-permission to all models.

'''
from django.db import models
from django.contrib.auth.models import User,Group
from django.conf import settings

class RestPermissions(models.Model):
    
    owner               = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related_owner") # CRUD
    # TODO : Shold this be one to many?
    group 		        = models.ForeignKey(Group,related_name="%(app_label)s_%(class)s_related_group")
    perms_octal_row     = models.CharField(blank=True, max_length=3) # 777 755 400
    perms_octal_field   = models.TextField(blank=True) # json list { "field_name": 777 , "another_field" : 755 , "other_field_name" : 400 }
    
    # NOTE : This is for example and should be in the extended model
    @property
    def perms_octal_default(self):
        return "700" # read / write / and edit/delete for user
    
    @property
    def perms_octal(self):
        
        # Default to no permissions
        perms = "000"
        
        # Set globabl perms
        if settings.REST_PERMISSION_DEFAULT:
            perms = settings.REST_PERMISSION_DEFAULT
            
        # Set model perms
        if self.perms_octal_default :
            perms = self.perms_octal_default
        
        # Set row perms
        if self.perms_octal_row != "" :
            perms = self.perms_octal_row
            
        # TODO
        # Set field perms    
        
    class Meta:
        abstract = True
        app_label='permission'
        
    # TODO - Why are we inhering from RESTEASY, instead of the other way around?
    def __init__(self, *args, **kwargs):
        super(RestEasy, self).__init__(*args, **kwargs)
    
    # overide editing at field level
    def save(self, *args, **kwargs):
        super(RestPermission, self).save(*args, **kwargs)

    # override reading at field level
    
#def get(instance, **kwargs):
#do stuff w/ instance.
    
# register 
#models.signals.post_init.connect(get, RestPermission)