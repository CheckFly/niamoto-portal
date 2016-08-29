# coding: utf-8

from rest_framework import viewsets

from apps.niamoto_data.models import Taxon, Occurrence
from apps.niamoto_data.serializers import TaxonSerializer, \
    OccurrenceSerializer


class TaxonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint for retrieving taxa.
    """
    base_name = 'taxon'
    queryset = Taxon.objects.all()
    serializer_class = TaxonSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        """
        Retrieve the list of taxa.
        """
        return super(TaxonViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a taxon given it's identifier.
        """
        return super(TaxonViewSet, self).retrieve(request, *args, **kwargs)


class OccurrenceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint for retrieving occurrences.
    """
    base_name = 'occurrence'

    def get_queryset(self):
        return Occurrence.objects.select_related('observations')

    def get_serializer(self, *args, **kwargs):
        incl_obs = self.request.query_params.get('include_observations', None)
        if incl_obs:
            kwargs['include_observations'] = True
        return OccurrenceSerializer(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        Retrieve the list of occurrences.
        """
        return super(TaxonViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve an occurrence given it's identifier.
        """
        return super(TaxonViewSet, self).retrieve(request, *args, **kwargs)
