"""results URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from schoolresults.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index , name="index" ),
    url(r'^register/$', register , name="register"),
    url(r'^login/$', login , name="login"),
    url(r'^semester/save/$', add_semester_save ),
    url(r'^semester/show/(?P<user>[^/]+)/(?P<name>[^/]+)$', show_semester , name="show-semester"),
    url(r'^profile/(?P<email>[^/]+)/$', show_profile , name="profile"),
    url(r'^semester/new/(?P<email>[^/]+)/$',add_semester, name='semester-add'),
    url(r'^semester/save/(?P<email>[^/]+)/$',add_semester_save, name='save-semester'),
    
]
