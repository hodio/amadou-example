from django.shortcuts       import render
from django.template.loader import get_template
from django.http            import HttpResponse
from django.template        import Context
from django.db              import models
from django.db.models       import get_models, get_app
from django.conf            import settings

# Create your views here.
def index(request):
    context = Context({'apps':getAppDictionary()})
    return render(request, 'index.html', context)

# This view converts native django models to ember models automatically
def emberModels(request):
    
    def generate(*app_list):
        
        # Initialize Dictionary
        ember_models = {}
        
        # Translate the Field Type django => ember
        FIELD_TRANSLATIONS = {
                              # FIELDS
                              "AutoField"                   : "DS.attr('number')",
                              "BooleanField"                : "DS.attr('boolean')",
                              "CharField"                   : "DS.attr('string')",
                              "DateField"                   : "DS.attr('date')",
                              "DateTimeField"               : "DS.attr('date')",
                              "DecimalField"                : "DS.attr('number')", # DOES EMBER SUPPORT DECIMALS?
                              "EmailField"                  : "DS.attr('string')",
                              "FileField"                   : "DS.attr('string')",
                              "FloatField"                  : "DS.attr('string')", # DOES EMBER SUPPORT FLOATS?
                              "ImageField"                  : "DS.attr('string')",
                              "IntegerField"                : "DS.attr('number')",
                              "IPAddressField"              : "DS.attr('string')",
                              "GenericIPAddressField"       : "DS.attr('string')",
                              "NullBooleanField"            : "DS.attr('boolean')",
                              "PositiveIntergeField"        : "DS.attr('number')",
                              "PositiveSmallIntegerField"   : "DS.attr('number')",
                              "SlugField"                   : "DS.attr('string')",
                              "SmallIntegerField"           : "DS.attr('number')",
                              "TextField"                   : "DS.attr('string')",
                              "TimeField"                   : "DS.attr('date')",
                              "URLField"                    : "DS.attr('string')",
                              # RELATIONSHIPS
                              "ForeignKey"                  : "DS.belongsTo('MODEL')", # !!! NOTE : Working here
                              "ManyToMany"                  : "DS.hasMany('MODEL')", # EXAMPLE App.Transaction
                              "OneToOneField"               : "DS.belongsTo('MODEL')"
                              }
        
        # Register All Models In Each App
        for app_name in app_list:
            app_models = get_app(app_name)
            for model in get_models(app_models):

                # Begin Ember Model Class 
                # !!! NOTE : If needed we can use appname here if we need to preserve non-core namespacing...)
                fields = {}
                for field in model._meta.fields:
                    
                    # Add Ember Fields ( !!! NOTE : Add restriction here to allow django based restriction of field exposure.)
                    field_type = field.get_internal_type()
                    
                    # Ember Uses id by default, so we don't define it
                    if field.name != 'id':
                        
                        # FIELDS
                        if 'Field' in field_type and 'OneToOneField' not in field_type:
                            fields[field.name] = FIELD_TRANSLATIONS.get(field_type)
                        # RELATIONSHIPS
                        else:
                            # NOTE : We have to treat these differently as some are defined as a string and others as a Class, hmmm...
                            if type (field.rel.to) is str :
                                related_model = field.rel.to.lower()
                            else:
                                related_model = field.rel.to.__name__.lower()
                            fields[field.name] = FIELD_TRANSLATIONS.get(field_type).replace('MODEL',related_model)
                # Add to Dictionary        
                ember_models[model.__name__] = fields
                
        return ember_models
    
    # Run the Register
    
    ember_models = generate(*settings.AMADOU_APPS)
    context = Context({'models':ember_models})
    return render(request, 'amadou_models.js', context)

def emberRoutes(request):

    context = Context({'apps':getAppDictionary()})
    return render(request, 'amadou_routes.js', context)

def emberRouter(request):
       
    context = Context({'apps':getAppDictionary()})
    return render(request, 'amadou_router.js', context)
    
def emberResources(request):
    
    # Initialize Dictionary
    ember_models = {}
    
    # Register All Models In Each App
    for app_name in settings.AMADOU_APPS:
        app_models = get_app(app_name)
        for model in get_models(app_models):

            # Add to Dictionary        
            ember_models[model.__name__.lower()] = model._meta.pk.attname
                
    
    # Run the Register
    context = Context({'models':ember_models})
    return render(request, 'amadou_resources.js', context)

def handlebarFilters(request):
    context = None
    return render(request,'amadou_filters.js',context)

# !!! NOTE : We need to refactor ALL above views to use this generated three dimensional dictionary
def getAppDictionary():
    
    apps = {}
    models = []
     # Register All Models In Each App
    for app_name in settings.AMADOU_APPS:
        
        models = {}
        app_models = get_app(app_name)
        for model in get_models(app_models):
            
            # Extract Fields
            fields = {}

            for field in model._meta.fields:
                    
                # Get Field TYpe & Append to the Dictionary
                field_type = str(field.get_internal_type())
                if field.name != 'id':
                    fields[field.name] = field_type
            
            # Add Fields to Model
            models[model.__name__.lower()] = fields
            
        # Add Models to App
        apps[app_name] = models
    
    return apps


# Technique of introspection of DRF
def get_form_parameters(self):

    """
    Builds form parameters from the serializer class
    """
    data = []
    serializer = self.get_serializer_class()

    if serializer is None:
        return data

    fields = serializer().get_fields()

    for name, field in fields.items():

        if getattr(field, 'read_only', False):
            continue

        data_type = field.type_label

        # guess format
        data_format = 'string'
        if data_type in self.PRIMITIVES:
            data_format = self.PRIMITIVES.get(data_type)[0]

        f = {
            'paramType': 'form',
            'name': name,
            'description': getattr(field, 'help_text', ''),
            'type': data_type,
            'format': data_format,
            'required': getattr(field, 'required', False),
            'defaultValue': get_resolved_value(field, 'default'),
        }

        # Min/Max values
        max_val = getattr(field, 'max_val', None)
        min_val = getattr(field, 'min_val', None)
        if max_val is not None and data_type == 'integer':
            f['minimum'] = min_val

        if max_val is not None and data_type == 'integer':
            f['maximum'] = max_val

        # ENUM options
        if field.type_label == 'multiple choice' \
                and isinstance(field.choices, list):
            f['enum'] = [k for k, v in field.choices]

        data.append(f)

    return data