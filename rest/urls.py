# coding: utf-8

from django.conf.urls import url, include

from rest.views import api_root


urlpatterns = [
    url(r'^$', api_root, name="api-root"),
    url(r'^docs/', include('rest_framework_docs.urls', namespace="docs")),
    url(r'^data/', include('apps.niamoto_data.rest_urls', namespace="data-api")),
    url(r'^plantnote/', include('apps.niamoto_plantnote.rest_urls', namespace="plantnote-api")),
    url(r'^forest_digitizing/', include('apps.forest_digitizing.rest_urls', namespace="forest_digitizing-api")),
    url(r'^rapid_inventory/', include('apps.rapid_inventories.rest_urls', namespace="rapid_inventory-api")),
    url(r'^management/', include('apps.niamoto_management.rest_urls', namespace="management-api")),
]
