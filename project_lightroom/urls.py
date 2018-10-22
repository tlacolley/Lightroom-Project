"""project_lightroom URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin
from light.views import LightListView, LightSwitchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LightListView.as_view(), name='list_light'),
    url(r'^light/(?P<pk>\d+)/switch$', LightSwitchView.as_view(), name='list_switch'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
