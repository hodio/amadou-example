from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered
from django.conf import settings
from django.db.models import get_models, get_app

 
from simple_history.admin import SimpleHistoryAdmin
 
def autoregister(*app_list):
    
    # Register All Models In Each App
    for app_name in app_list:
        app_models = get_app(app_name)
        
        # Loop through models, and register
        for model in get_models(app_models):
   
   			# Register model as a Simple History Admin
            try: 
                admin.site.register(model,SimpleHistoryAdmin)
            except AlreadyRegistered:
                pass

# Run the Register
autoregister(*settings.REST_EASY_APPS)
