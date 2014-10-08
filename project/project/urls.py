from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
                  
    # Admin
    url(r'^api/admin/', include(admin.site.urls)),
    
    # Load Amadou URLs (Django Rest Framework Endpoints)
    url(r'^', include('rest_easy.urls')), 
)

