"""imdapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from imd import views

urlpatterns = [
    # Admin page
    url(r'^admin/', admin.site.urls),
    # Index page
    url(r'^$', views.index, name='index'),
    # Services pages
    url(r'^services/$', views.services, name='services'),
    url(r'^services/vehicle-wraps/$', views.vehicle_wraps, name='vehicle_wraps'),
    url(r'^services/tradeshows/$', views.tradeshows, name='tradeshows'),
    url(r'^services/web-design/$', views.web_design, name='web_design'),
    url(r'^services/design-service/$', views.design_service, name='design_service'),
    url(r'^services/signs-banners/$', views.signs_banners, name='signs_banners'),
    url(r'^services/printing/$', views.printing, name='printing'),
    url(r'^services/photography/$', views.photography, name='photography'),
    url(r'^service/window-wall-floor/$', views.window_wall_floor, name='window_wall_floor'),
    # Gallery Page
    url(r'^gallery/$', views.gallery, name="gallery"),
    # Contact Page
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact_form/$', views.index, name='contact_form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

