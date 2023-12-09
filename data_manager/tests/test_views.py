from django.test import TestCase
from django.test.client import RequestFactory
from data_manager.models import Layer
from data_manager.views import get_json
from collections.abc import Collection, Mapping
import json

from data_manager.models import Layer

class get_layer_details_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        congress_layer_url="https://coast.noaa.gov/arcgis/rest/services/OceanReports/USCongressionalDistricts/MapServer/export"
        Layer.objects.create(pk=1, name='arcrest_layer', layer_type='ArcRest', url=congress_layer_url, arcgis_layers="0", maxZoom=14, minZoom=6)

    def test_view_api_returns_zoom_limits(self):
        response = self.client.get('/data_manager/get_layer_details/1')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.getvalue())
        self.assertTrue('name' in result.keys())
        self.assertEqual(result['name'], 'arcrest_layer')
        #checking that the attribute EXISTS in result.keys, if it does exist, it returns true
        self.assertTrue('minZoom' in result.keys())
        self.assertTrue('maxZoom' in result.keys())
        self.assertEqual(result['minZoom'], 6)
        self.assertEqual(result['maxZoom'], 14)
        print('Hello World')

class data_manager_get_json_test(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_view_api_returns_zoom_limits(self):
        # Create an instance of a GET request.
        request = self.factory.get('/data_manager/get_json')
        request.META['HTTP_HOST'] = "localhost:8000"
        response = get_json(request)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        # Make sure response contains "success", "state", "layers" and "themes" 
        self.assertIn("success", result)
        self.assertIn("state", result)
        self.assertIn("layers", result)
        self.assertIn("themes", result)

        self.assertTrue(result['success'])
        self.assertIsInstance(result['layers'], Collection)
        self.assertIsInstance(result['themes'], Collection)
        self.assertIsInstance(result['state'], Mapping)
      