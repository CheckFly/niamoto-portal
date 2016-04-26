# coding: utf-8

from django.conf import settings
from django.db import connection
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ncbif_taxa.models import Taxon
from ncbif_occurrences.models import Occurrence
from restapi.serializers import TaxonSerializer, OccurrenceSerializer
from utils import dict_fetchall


class TaxonViewSet(viewsets.ModelViewSet):
    base_name = 'taxon'
    queryset = Taxon.objects.all()
    serializer_class = TaxonSerializer


class OccurrenceViewSet(viewsets.ViewSet):
    """
    ViewSet for listing or retrieving occurrences.
    """

    base_name = 'occurrence'

    def list(self, request):
        host = request.get_host()
        hlink = 'http://{}/{}/{}/'.format(
            host,
            settings.REST_API_BASE_URL,
            TaxonViewSet.base_name
        )
        cursor = connection.cursor()
        fields = (
            'id',
            'date',
            "'{}'::text || taxon_id::text || '/' AS taxon".format(hlink),
            'ST_AsEWKT(location) AS location'
        )
        db_table = Occurrence._meta.db_table
        cursor.execute('SELECT {} FROM {}'.format(','.join(fields), db_table))
        data = dict_fetchall(cursor)
        return Response(data)

    def retrieve(self, request, pk=None):
        queryset = Occurrence.objects.all()
        occurrence = get_object_or_404(queryset, pk=pk)
        serializer = OccurrenceSerializer(
            occurrence,
            context={'request': request}
        )
        return Response(serializer.data)