# coding: utf-8

from rest_framework import viewsets
from rest_framework import filters

from niamoto_data.models import Taxon, Occurrence, Massif
from niamoto_plantnote.models import PlantnoteDatabase
from rapid_inventories.models import RapidInventory
from rapid_inventories.serializers import RapidInventorySerializer
from restapi.serializers import TaxonSerializer, OccurrenceSerializer, \
    PlantnoteDatabaseSerializer, MassifSerializer


class TaxonViewSet(viewsets.ReadOnlyModelViewSet):
    base_name = 'taxon'
    queryset = Taxon.objects.all()
    serializer_class = TaxonSerializer


class OccurrenceViewSet(viewsets.ReadOnlyModelViewSet):
    base_name = 'occurrence'
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer


class MassifViewSet(viewsets.ReadOnlyModelViewSet):
    base_name = 'massif'
    queryset = Massif.objects.all()
    serializer_class = MassifSerializer


class PlantnoteDatabaseViewSet(viewsets.ReadOnlyModelViewSet):
    base_name = 'plantnote_database'
    queryset = PlantnoteDatabase.objects.all()
    serializer_class = PlantnoteDatabaseSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('active', )


class RapidInventoryViewSet(viewsets.ReadOnlyModelViewSet):
    base_name = 'rapid_inventory'
    queryset = RapidInventory.objects.all()
    serializer_class = RapidInventorySerializer
