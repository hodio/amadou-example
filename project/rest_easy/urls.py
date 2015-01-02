from django.conf.urls import url, include
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.throttling import UserRateThrottle
import re

# Permissions
import permission
permission.autodiscover()
from django.conf            import settings
from django.db.models       import get_models, get_app

from resources import modelResources

# !!! DEBUG
import logging
logger = logging.getLogger(__name__)
# !!! NED DEBUG

# User Serialization
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model   = User
        fields  = ('url', 'username', 'email', 'is_staff')
        
class UserViewSet(viewsets.ModelViewSet):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Import Model Resource Generator & Register w/ django-rest-framework
model_resources = modelResources()
for class_name, class_object in model_resources.iteritems():
    router.register(r''+class_name, class_object)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
               
    # Endpoints
    url(r'^api/', include(router.urls)),
    
    # Auth
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # OAuth
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    
]