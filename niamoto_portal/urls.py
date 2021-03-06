"""niamoto_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from apps.portal import views
from apps.data_plot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.portal.urls')),
    path('peuplement/', include('apps.data_plot.urls', namespace='plot')),
    path('forets/', include('apps.data_shape.urls', namespace='shape')),
    path('arbres/', include('apps.data_taxon.urls', namespace='taxon')),
    path(f'{settings.REST_API_BASE_URL}/', include('apps.api_rest.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
