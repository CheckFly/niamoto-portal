# coding: utf-8

import json

from niamoto.api.data_marts_api import get_dimension, get_dimensional_model
from cubes import PointCut, Cell

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view


@method_decorator(login_required, name='dispatch')
class DataMartView(TemplateView):
    """
    Class-based view for plot dashboards page.
    """
    template_name = "data_marts/data_mart.html"

    def get_context_data(self, **kwargs):
        return {
            'props': json.dumps({
                'provinces': get_province_levels(),
                'massifs': get_massif_levels(),
                'communes': get_commune_levels(),
            }),
        }


@api_view(['GET'])
def process(request):
    agg = [
        {
            "name": "occurrence_sum",
            "function": "sum",
            "measure": "occurrence_count",
        },
    ]
    dm = get_dimensional_model(
        'taxon_observed_occurrences',
        agg,
    )
    workspace = dm.get_cubes_workspace()
    cube = workspace.cube('taxon_observed_occurrences')
    browser = workspace.browser(cube)
    selected_entity = json.loads(
        request.query_params.get('selected_entity', None)
    )
    cuts = [
        PointCut(selected_entity['type'], [selected_entity['value']]),
    ]
    cell = Cell(cube, cuts)
    result = browser.aggregate(cell, drilldown=['taxon_dimension'])
    return Response({
        'summary': result.summary,
        'records': list(result),
    })


def get_province_levels():
    province_dim = get_dimension('provinces')
    labels = province_dim.get_labels()
    labels = [(str(k), v) for k, v in labels.to_dict().items()]
    return labels


def get_massif_levels():
    return [None]


def get_commune_levels():
    commune_dim = get_dimension('communes')
    labels = commune_dim.get_labels()
    labels = [(str(k), v) for k, v in labels.to_dict().items()]
    return labels


class DimensionViewSet(ViewSet):
    """
    Base class for dimension ViewSet.
    """

    def __init__(self, dimension_name, *args, **kwargs):
        self.dimension_name = dimension_name
        self._data = None
        super(DimensionViewSet, self).__init__(*args, **kwargs)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def retrieve(self, request, pk=None):
        if self.data is None:
            self.data = get_dimension(self.dimension_name).get_values()
        return Response(self.data[self.data.index == int(pk)].to_json())

    def list(self, request):
        if self.data is None:
            self.data = get_dimension(self.dimension_name).get_values()
        return Response(self.data.to_json())


class ProvinceDimensionViewSet(DimensionViewSet):
    """
    Province Dimension ViewSet.
    """

    def __init__(self, *args, **kwargs):
        super(ProvinceDimensionViewSet, self).__init__(
            'provinces',
            *args,
            **kwargs
        )

    @DimensionViewSet.data.setter
    def data(self, value):
        self._data = value.simplify(0.01)


class CommuneDimensionViewSet(DimensionViewSet):
    """
    Commune Dimension Viewset.
    """

    def __init__(self, *args, **kwargs):
        super(CommuneDimensionViewSet, self).__init__(
            'communes',
            *args,
            **kwargs
        )

    @DimensionViewSet.data.setter
    def data(self, value):
        self._data = value.simplify(0.005)
