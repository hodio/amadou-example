from permission.logics import AuthorPermissionLogic, CollaboratorsPermissionLogic, GroupInPermissionLogic, StaffPermissionLogic
from django.conf            import settings
from django.db.models       import get_models, get_app
'''
EXAMPLE
PERMISSION_LOGICS = (
    ('example.Person', AuthorPermissionLogic(field_name='owner',)),
    ('example.Person', CollaboratorsPermissionLogic()),
)
'''

# Loop the registered apps from settings
for app_name in settings.REST_EASY_APPS:
        
    # Get the models, then loop
    PERMISSION_LOGICS = ()
    app_models = get_app(app_name)
    for app_model in get_models(app_models):
    	PERMISSION_LOGICS = PERMISSION_LOGICS + (( app_name+'.'+app_model.__name__,AuthorPermissionLogic(field_name='owner'),),)
    	PERMISSION_LOGICS = PERMISSION_LOGICS + (( app_name+'.'+app_model.__name__,CollaboratorsPermissionLogic(),),)
    	#PERMISSION_LOGICS = PERMISSION_LOGICS + (( app_name+'.'+app_model.__name__,GroupInPermissionLogic(),),)
    	PERMISSION_LOGICS = PERMISSION_LOGICS + (( app_name+'.'+app_model.__name__,StaffPermissionLogic(),),)
