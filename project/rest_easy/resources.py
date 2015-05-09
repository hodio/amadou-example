from django.conf            import settings
from django.db.models       import get_models, get_app

from rest_framework import routers, serializers, viewsets
from rest_framework.throttling import UserRateThrottle
import re

def modelResources():
    
    model_resources = {}
    
    # Loop the registered apps from settings
    for app_name in settings.REST_EASY_APPS:
        
        # Get the models, then loop
        app_models = get_app(app_name)
        for app_model in get_models(app_models):
            
            # Assemble fields into a tuple
            model_fields = ()
            model_filter_fields = ()
            for field in app_model._meta.fields:
                if field.name != 'id':
                    model_fields = model_fields + (field.name,)

            # Assemble Properties into a dictionary
            model_properties = {}
            for attribute in dir(app_model):
                # Ignore hidden attributes and the primary key
                if attribute[0:1] != '_' and attribute != 'pk':
                    try:
                        attribute_value = getattr(app_model,attribute)
                        if isinstance(attribute_value,property):
                            model_properties[attribute] = attribute
                    except:
                        pass

            # Instantiate Dictionary
            serializer_dictionary = {}
            
            # Creat the class properties, append to dictionary also append to field names
            for property_name in model_properties:
                serializer_dictionary[property_name] = serializers.Field(source=property_name)

            # Create Django Rest Framework Serializer
            class_name = app_model.__name__+'Serializer'
            class Meta:
                 model  = app_model
                 # !!! NEED TO DETERMINE USAGE FOR THIS
                 # currently if disabled will show all fields, when do we want to show collabs?
                 #fields = model_fields # !!! Is this needed?
               
            # Add meta class to dictionary
            serializer_dictionary['Meta'] = Meta
            serializer = type(class_name,(serializers.HyperlinkedModelSerializer,), serializer_dictionary) 
            
            # Create DRF Viewset
            class_name = app_model.__name__.lower()
            if type(app_model._meta.verbose_name_plural) is str: # Inherit Plural (If set)
                class_name = app_model._meta.verbose_name_plural

            queryset = app_model.objects.all()

            # Create class and add to dictionary
            # Check pattern from REST_EASY_IGNORE_APPS in settings.
            ignore = False
            try:
                settings.REST_EASY_IGNORE_MODELS
            except:
                pass
            else:
                for ignore_pattern in settings.REST_EASY_IGNORE_MODELS:
                    if re.match(ignore_pattern,app_model.__name__) is not None:
                        ignore = True
            if not ignore: 

                # Create DRF ViewSet
                model_resources[class_name] = type(class_name,(viewsets.ModelViewSet,), {
                    'queryset'          : queryset,
                    'serializer_class'  : serializer,
                    'filter_fields'     : model_fields,
                    'throttle_classes'  : (UserRateThrottle,) # !!! NOTE : This neees to be dyanmic
                }) 
            
    return model_resources