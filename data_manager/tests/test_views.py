from django.test import TestCase
from django.test.client import RequestFactory
from data_manager.models import Layer, Theme
from data_manager.views import get_json, get_themes
from collections.abc import Collection, Mapping
from django.contrib.sites.models import Site
import json


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
        # Checking that the attribute EXISTS in result.keys, if it does exist, it returns true
        self.assertTrue('minZoom' in result.keys())
        self.assertTrue('maxZoom' in result.keys())
        self.assertEqual(result['minZoom'], 6)
        self.assertEqual(result['maxZoom'], 14)

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

class DataManagerGetThemesTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()  
        # Associate theme with default site id, otherwise themes do not show up
        Theme.objects.create(id=1, name="test", display_name="test", visible=True).site.set([1,])
        Theme.objects.create(id=2, name="test2", display_name="test2", visible=True).site.set([1,])

    def test_get_themes_response_format(self):
        request = self.factory.get('/data_manager/get_themes')
        request.META['HTTP_HOST'] = "localhost:8000" 

        response = get_themes(request)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        self.assertIn('themes', result, "Response should contain 'themes' key")

        # Get the list of themes from the response
        themes = result['themes']

        # Check if the themes is a list
        self.assertTrue(isinstance(themes, list), "Themes should be a list")
        self.assertTrue(len(themes)==2)

        # Check the format of each theme object in the list
        for theme in themes:
            self.assertTrue(isinstance(theme, dict), "Each theme should be a dictionary")

            self.assertIn('id', theme, "Theme should have 'id' key")
            self.assertIn('name', theme, "Theme should have 'name' key")
            self.assertIn('display_name', theme, "Theme should have 'display_name' key")
            self.assertIn('is_visible', theme, "Theme should have 'is_visible' key")

            self.assertTrue(isinstance(theme['id'], int), "id should be an integer")
            self.assertTrue(isinstance(theme['name'], str), "name should be a string")
            self.assertTrue(isinstance(theme['display_name'], str), "display_name should be a string")
            self.assertTrue(isinstance(theme['is_visible'], bool), "is_visible should be a boolean")

    def test_get_themes_response_data(self):
        request = self.factory.get('/data_manager/get_themes')
        request.META['HTTP_HOST'] = "localhost:8000"

        response = get_themes(request)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        self.assertIn('themes', result, "Response should contain 'themes' key")

        # Get the specific themes from the response to test data 
        theme_1 = result['themes'][0]
        theme_2 = result['themes'][1]

        # Check the format of each theme object in the list - similar to first
        self.assertEqual(theme_1["id"], 1)
        self.assertEqual(theme_1["name"], "test")
        self.assertEqual(theme_1["display_name"], "test")
        self.assertTrue(theme_1["is_visible"])

        self.assertEqual(theme_2["id"], 2)
        self.assertEqual(theme_2["name"], "test2")
        self.assertEqual(theme_2["display_name"], "test2")
        self.assertTrue(theme_2["is_visible"])

class DataManagerGetLayerSearchData(TestCase):
     def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()  
        theme1 = Theme.objects.create(id=3, name="test3", display_name="test3", visible=True, description="test 3").site.set([1,])
        theme2 = Theme.objects.create(id=4, name="test4", display_name="test4", visible=True, description="test 4").site.set([1,])
        layer1 = Layer.objects.create(id=5, name="layertest1", is_sublayer=False).themes.set([theme1, ])
        layer2 = Layer.objects.create(id=6, name="layertest2", is_sublayer=True).subLayers.set([layer1, ])
        layer2.themes.set([theme1, ])
        layer3 = Layer.objects.create(id=7, name="layertest3", is_sublayer=False).themes.set([theme2, ])

     def test_get_layer_search_data_response_format(self):
        request = self.factory.get('/data_manager/get_layer_search_data')
        request.META['HTTP_HOST'] = "localhost:8000" 

        response = get_themes(request)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        print(result)



      