"""
URL configuration for suorganizer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from .views import redirect_root
from django.views.generic import RedirectView, TemplateView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', RedirectView.as_view(pattern_name='blog_post_list', permanent=False)),
    path('', include('organizer.urls')),
    path('about/', TemplateView.as_view(template_name='site/about.html'), name='about_site'),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),  
    #path('user/', include(user_urls, app_name='user', namespace='dj-auth')), 
    path('', include('user.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Startup Organizer Admin'
admin.site.site_title = 'Startup Organizer'