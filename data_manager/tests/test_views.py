from django.test import TestCase
from django.test.client import RequestFactory
from data_manager.models import Layer, Theme
from data_manager.views import get_json, get_themes
from collections.abc import Collection, Mapping
from django.contrib.sites.models import Site
import json

class get_layer_details_test(TestCase):
    def setUp(self):
        congress_layer_url="https://coast.noaa.gov/arcgis/rest/services/OceanReports/USCongressionalDistricts/MapServer/export"
        theme1 = Theme.objects.create(id=1, name="companion", display_name="companion", visible=True)
        theme1.site.set([1])
        # This test layer will have attributes defined to test data type when filled out
        layer1 =Layer.objects.create(id=1, name='arcrest_layer', order=15, layer_type="arcgis", url=congress_layer_url, arcgis_layers="19", password_protected=True, query_by_point=True,  maxZoom=14, minZoom=6, proxy_url=True, disable_arcgis_attributes=True, utfurl="testing", wms_slug="hi", wms_version="hello", 
                             wms_format="pusheen", wms_srs="world", wms_styles="style", wms_timing="hullo", wms_time_item="ello", wms_additional="star", wms_info=True, wms_info_format="test", has_companion=True, search_query=True, legend="hi", legend_title="title", legend_subtitle="subtitle", description="testlayer", 
                             data_overview="testlayer", data_source="testlayer", data_notes="testlayer", kml="testlayer", data_download="testlayer", learn_more="testlayer", metadata="testlayer", source="testlayer", label_field="testlayer", custom_style="testlayer", vector_outline_color="blue", vector_outline_opacity=5, vector_outline_width=2, point_radius=8,
                             vector_color="blue", vector_fill=5, vector_graphic="testlayer", vector_graphic_scale=5, opacity=0.8, is_annotated=True, is_disabled=True, disabled_message="testlayer")
        # This test layer will not have attributes defined other than required fields to test default behavior when attributes left empty
        layer1.site.set([1])
        layer2 = Layer.objects.create(id=2, name="Arc", layer_type="arcgis")
        layer2.themes.set([1])
        layer2.site.set([1])
        layer3 = Layer.objects.create(id=3, name="sublayer", layer_type="arcgis", is_sublayer=True)
        layer3.site.set([1])
        layer2.connect_companion_layers_to.set([layer1])
        layer1.sublayers.set([layer3])
    
    def test_view_api_returns_zoom_limits(self):
        response = self.client.get('/data_manager/get_layer_details/1')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)

        self.assertTrue('name' in result.keys())
        self.assertEqual(result['name'], 'arcrest_layer')
        # Checking that the attribute EXISTS in result.keys, if it does exist, it returns true
        self.assertTrue('minZoom' in result.keys())
        self.assertTrue('maxZoom' in result.keys())
        self.assertEqual(result['minZoom'], 6)
        self.assertEqual(result['maxZoom'], 14)
    
    def test_view_layer_details_response_format(self):
        response1 = self.client.get('/data_manager/get_layer_details/1')
        self.assertEqual(response1.status_code, 200)
        result1 = json.loads(response1.content)

        response2 = self.client.get('/data_manager/get_layer_details/2')
        self.assertEqual(response2.status_code, 200)
        result2 = json.loads(response2.content)

        layer_attr = ["id", "uuid", "name", "order", "type", "arcgis_layers", "url", "password_protected", "query_by_point", "proxy_url", "disable_arcgis_attributes", "wms_slug", "wms_version", "wms_format", "wms_srs", "wms_styles", "wms_timing", "wms_time_item", "wms_additional", "wms_info", 
                            "wms_info_format", "utfurl", "subLayers", "companion_layers", "has_companion", "queryable", "legend", "legend_title", "legend_subtitle", "show_legend", "description", "overview", "data_source", "data_notes", "kml", "data_download", 
                            "learn_more", "metadata", "source", "tiles", "label_field", "attributes", "minZoom", "maxZoom", "lookups", "custom_style", "outline_color", "outline_opacity", "outline_width", "point_radius", "color", "fill_opacity", "graphic", "graphic_scale", "opacity",
                            "annotated", "is_disabled", "disabled_message", "data_url", "is_multilayer", "is_multilayer_parent", "dimensions", "associated_multilayers", "catalog_html", "parent", "date_modified"]

        for i in layer_attr:
            self.assertIn(i, result1)
            self.assertIn(i, result2)
        
        results = [result1, result2]

        for i in results:
            self.assertIsInstance(i["id"], int, "id should be int")
            self.assertIsInstance(i["uuid"], str, "uuid should be string")
            self.assertIsInstance(i["name"], str, "name should be string") 
            self.assertIsInstance(i["order"], int, "order should be int")
            self.assertIsInstance(i["type"], str, "type should be string")
            self.assertIsInstance(i["arcgis_layers"], (str, type(None)), "arcgis_layers should be string or none")
            self.assertIsInstance(i["url"], str, "url should be string")
            self.assertIsInstance(i["password_protected"], bool, "password_protected should be boolean")
            self.assertIsInstance(i["query_by_point"], bool, "query_by_point should be boolean")
            self.assertIsInstance(i["proxy_url"], bool, "proxy_url should be boolean")
            self.assertIsInstance(i["disable_arcgis_attributes"], bool, "disable_arcgis_attributes should be boolean" )
            self.assertIsInstance(i["wms_slug"], (str, type(None)), "wms_slug should be string or none" )
            self.assertIsInstance(i["wms_version"], (str, type(None)), "wms_version should be string or none")
            self.assertIsInstance(i["wms_format"], (str, type(None)), "wms_format should be string or none")
            self.assertIsInstance(i["wms_srs"], (str, type(None)), "wms_srs should be string or none")
            self.assertIsInstance(i["wms_styles"], (str, type(None)), "wms_styles should be string or none")
            self.assertIsInstance(i["wms_timing"], (str, type(None)), "wms_timing should be string or none")
            self.assertIsInstance(i["wms_time_item"], (str, type(None)), "wms_time_item should be string or none")
            self.assertIsInstance(i["wms_additional"], (str, type(None)), "wms_additional should be string or none")
            self.assertIsInstance(i["wms_info"], bool, "wms_info should be boolean")
            self.assertIsInstance(i["wms_info_format"], (str, type(None)), "wms_info_format should be string or none")
            self.assertIsInstance(i["utfurl"], (str, type(None)), "utfurl should be string or none")
            self.assertIsInstance(i["subLayers"], Collection, "subLayers should be a collection")
            self.assertIsInstance(i["companion_layers"], Collection, "companion_layers should be collection")
            self.assertIsInstance(i["has_companion"], bool, "has_companion should be bool")
            self.assertIsInstance(i["queryable"], bool, "queryable should be boolean")
            self.assertIsInstance(i["legend"], (str, type(None)), "legend should be string")
            self.assertIsInstance(i["legend_title"], (str, type(None)), "legend_title should be string or none")
            self.assertIsInstance(i["legend_subtitle"], (str, type(None)), "legend_subtitle should be string or none")
            self.assertIsInstance(i["show_legend"], bool, "show_legend should be bool" )
            self.assertIsInstance(i["description"], (str, type(None)), "description should be string or none" )
            self.assertIsInstance(i["overview"], (str, type(None)), "overview should be string or none")
            self.assertIsInstance(i["data_source"], (str, type(None)), "data_source should be string or none")
            self.assertIsInstance(i["data_notes"], (str, type(None)), "data_notes should be string or none" )
            self.assertIsInstance(i["kml"], (str, type(None)), "kml should be string or none")
            self.assertIsInstance(i["data_download"], (str, type(None)), "data_download should be string or none")
            self.assertIsInstance(i["learn_more"], (str, type(None)), "learn_more should be string or none")
            self.assertIsInstance(i["metadata"], (str, type(None)), "metadata should be string or none")
            self.assertIsInstance(i["source"], (str, type(None)), "source should be string or none")
            self.assertIsInstance(i["tiles"], (str, type(None)), "tiles should be string or none")
            self.assertIsInstance(i["label_field"], (str, type(None)), "label_field should be string or none")
            self.assertIsInstance(i["attributes"], dict, "attributes should be dictionary (JSON object)")
            self.assertIsInstance(i["minZoom"], (float, type(None)), "minZoom should be float")
            self.assertIsInstance(i["maxZoom"], (float, type(None)), "maxZoom should be float")
            self.assertIsInstance(i["lookups"], dict, "lookups should be dictionary(JSON object)")
            self.assertIsInstance(i["custom_style"], (str, type(None)), "custom_style should be string or none")
            self.assertIsInstance(i["outline_color"], (str, type(None)), "outline_color should be string or none")
            self.assertIsInstance(i["outline_opacity"], (float, type(None)), "outline_opacity should be float or none")
            self.assertIsInstance(i["outline_width"], (int, type(None)), "outline_width should be int or none")
            self.assertIsInstance(i["point_radius"], (int, type(None)), "point_radius should be int or none")
            self.assertIsInstance(i["color"], (str, type(None)), "color should be string or none")
            self.assertIsInstance(i["fill_opacity"], (float, type(None)), "fill_opacity should be float or none")
            self.assertIsInstance(i["graphic"], (str, type(None)), "graphic should be string or none")
            self.assertIsInstance(i["graphic_scale"], (float), "graphic_scale should be float")
            self.assertIsInstance(i["opacity"], float, "opacity should be float")
            self.assertIsInstance(i["annotated"], bool, "annotated should be bool")
            self.assertIsInstance(i["is_disabled"], bool, "is_disabled should be bool")
            self.assertIsInstance(i["disabled_message"], (str, type(None)), "disabled_message should be string or none")
            self.assertIsInstance(i["data_url"], (str, type(None)), "data_url should be string or none")
            self.assertIsInstance(i["is_multilayer"], bool, "is_multilayer should be bool")
            self.assertIsInstance(i["is_multilayer_parent"], bool, "is_multilayer_parent should be bool")
            self.assertIsInstance(i["dimensions"], Collection, "dimensions should be collection")
            self.assertIsInstance(i["associated_multilayers"], dict, "associated_multilayers should be dictionary")
            self.assertIsInstance(i["catalog_html"], str, "catalog_html should be string")
            self.assertIsInstance(i["parent"], (dict, type(None)), "parent should be dictionary(JSON object) or none")
            self.assertIsInstance(i["date_modified"], str, "date_modified should be string")
    
    def test_view_layer_details_default_response_data(self):
        response = self.client.get('/data_manager/get_layer_details/2')
        self.assertEqual(response.status_code, 200)
        result= json.loads(response.content)
        expected_attributes = {'compress_attributes': False, 'event': 'click', 'attributes': [], 'mouseover_attribute': None, 'preserved_format_attributes': []}
        expected_lookups = {'field': None, 'details': []}

        self.assertEqual(result["id"], 2)
        self.assertEqual(result["name"], "Arc")
        self.assertEqual(result["order"], 10)
        self.assertEqual(result["type"], "arcgis")
        self.assertEqual(result["url"], "")
        self.assertEqual(result["arcgis_layers"], None)
        self.assertEqual(result["password_protected"], False)
        self.assertEqual(result["query_by_point"], False)
        self.assertEqual(result["proxy_url"], False)
        self.assertEqual(result["disable_arcgis_attributes"], False)
        self.assertEqual(result["wms_slug"], None)
        self.assertEqual(result["wms_version"], None)
        self.assertEqual(result["wms_format"], None)
        self.assertEqual(result["wms_srs"], None)
        self.assertEqual(result["wms_styles"], None)
        self.assertEqual(result["wms_timing"], None)
        self.assertEqual(result["wms_time_item"], None)
        self.assertEqual(result["wms_additional"], None)
        self.assertEqual(result["wms_info"], False)
        self.assertEqual(result["wms_info_format"], None)
        self.assertEqual(result["utfurl"], None)
        self.assertEqual(result["subLayers"], [])
        self.assertEqual(result["has_companion"], False)
        self.assertEqual(result["queryable"], False)
        self.assertEqual(result["legend"], None)
        self.assertEqual(result["legend_title"], None)
        self.assertEqual(result["legend_subtitle"], None)
        self.assertEqual(result["show_legend"], True)
        self.assertEqual(result["description"], None)
        self.assertEqual(result["overview"], None)
        self.assertEqual(result["data_source"], None)
        self.assertEqual(result["data_notes"], None)
        self.assertEqual(result["kml"], None)
        self.assertEqual(result["data_download"], None)
        self.assertEqual(result["learn_more"], None)
        self.assertEqual(result["metadata"], None)
        self.assertEqual(result["source"], None)
        self.assertEqual(result["tiles"], None)
        self.assertEqual(result["label_field"], None)
        self.assertEqual(result["attributes"], expected_attributes)
        self.assertEqual(result["lookups"], expected_lookups)
        self.assertEqual(result["minZoom"], None)
        self.assertEqual(result["maxZoom"], None)
        self.assertEqual(result["custom_style"], None)
        self.assertEqual(result["outline_color"], None)
        self.assertEqual(result["outline_opacity"], None)
        self.assertEqual(result["outline_width"], None)
        self.assertEqual(result["point_radius"], None)
        self.assertEqual(result["color"], None)
        self.assertEqual(result["fill_opacity"], None)
        self.assertEqual(result["graphic"], None)
        self.assertEqual(result["graphic_scale"], 1.0)
        self.assertEqual(result["opacity"], 0.5)
        self.assertEqual(result["annotated"], False)
        self.assertEqual(result["is_disabled"], False)
        self.assertEqual(result["disabled_message"], None)
        self.assertEqual(result["data_url"], "/data-catalog/companion/#layer-info-arc2")
        self.assertEqual(result["is_multilayer"], False)
        self.assertEqual(result["is_multilayer_parent"], False)
        self.assertEqual(result["dimensions"], [])
        self.assertEqual(result["associated_multilayers"], {})
        self.assertEqual(result["parent"], None)

    def test_view_layer_details_response_data(self):
        response = self.client.get('/data_manager/get_layer_details/1')
        self.assertEqual(response.status_code, 200)
        result= json.loads(response.content)
        congress_layer_url="https://coast.noaa.gov/arcgis/rest/services/OceanReports/USCongressionalDistricts/MapServer/export"
        layer3 = Layer.objects.get(id=3)
        layer3dict = layer3.toDict
        layer3dict["uuid"] = str(layer3dict["uuid"])
        layer3dict["parent"]["uuid"] = str(layer3dict["parent"]["uuid"])
        layer3dict["parent"]["subLayers"][0]["uuid"] = str(layer3dict["parent"]["subLayers"][0]["uuid"] )
        layer2 = Layer.objects.get(id=2)
        layer2dict = layer2.toDict
        layer2dict["uuid"] = str(layer2dict["uuid"])
        expected_attributes = {'compress_attributes': False, 'event': 'click', 'attributes': [], 'mouseover_attribute': None, 'preserved_format_attributes': []}
        expected_lookups = {'field': None, 'details': []}

        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "arcrest_layer")
        self.assertEqual(result["order"], 15)
        self.assertEqual(result["type"], "arcgis")
        self.assertEqual(result["url"], congress_layer_url)
        self.assertEqual(result["arcgis_layers"], "19")
        self.assertEqual(result["password_protected"], True)
        self.assertEqual(result["query_by_point"], True)
        self.assertEqual(result["proxy_url"], True)
        self.assertEqual(result["disable_arcgis_attributes"], True)
        self.assertEqual(result["wms_slug"], "hi")
        self.assertEqual(result["wms_version"], "hello")
        self.assertEqual(result["wms_format"], "pusheen")
        self.assertEqual(result["wms_srs"], "world")
        self.assertEqual(result["wms_styles"], "style")
        self.assertEqual(result["wms_timing"], "hullo")
        self.assertEqual(result["wms_time_item"], "ello")
        self.assertEqual(result["wms_additional"], "star")
        self.assertEqual(result["wms_info"], True)
        self.assertEqual(result["wms_info_format"], "test")
        self.assertEqual(result["utfurl"], "testing")
        for key in result["subLayers"][0].keys():
            #description and overview takes from parent, but parent should not be set
            if not key in ["is_sublayer", "date_modified", "companion_layers", "description", "overview"]:
                if key != "parent":
                    self.assertEqual(result["subLayers"][0][key], layer3dict[key])
                else:
                    self.assertEqual(result["subLayers"][0][key], layer3dict[key]["id"])
        for key in result["companion_layers"][0].keys():
            #layer_dict does not have is_sublayer
            if not key in ["is_sublayer", "date_modified", "companion_layers", "parent"]:
                self.assertEqual(result["companion_layers"][0][key], layer2dict[key])
        self.assertEqual(result["has_companion"], True)
        self.assertEqual(result["queryable"], True)
        self.assertEqual(result["legend"], "hi")
        self.assertEqual(result["legend_title"], "title")
        self.assertEqual(result["legend_subtitle"], "subtitle")
        self.assertEqual(result["show_legend"], True)
        self.assertEqual(result["description"], "testlayer")
        self.assertEqual(result["overview"], "testlayer")
        self.assertEqual(result["data_source"], "testlayer")
        self.assertEqual(result["data_notes"], "testlayer")
        self.assertEqual(result["kml"], "testlayer")
        self.assertEqual(result["data_download"], "testlayer")
        self.assertEqual(result["learn_more"], "testlayer")
        self.assertEqual(result["metadata"], "testlayer")
        self.assertEqual(result["source"], "testlayer")
        self.assertEqual(result["tiles"], None)
        self.assertEqual(result["label_field"], "testlayer")
        self.assertEqual(result["attributes"], expected_attributes)
        self.assertEqual(result["lookups"], expected_lookups)
        self.assertEqual(result["minZoom"], 6)
        self.assertEqual(result["maxZoom"], 14)
        self.assertEqual(result["custom_style"], "testlayer")
        self.assertEqual(result["outline_color"], "blue")
        self.assertEqual(result["outline_opacity"], 5.0)
        self.assertEqual(result["outline_width"], 2)
        self.assertEqual(result["point_radius"], 8)
        self.assertEqual(result["color"], "blue")
        self.assertEqual(result["fill_opacity"], 5.0)
        self.assertEqual(result["graphic"], "testlayer")
        self.assertEqual(result["graphic_scale"], 5.0)
        self.assertEqual(result["opacity"], 0.8)
        self.assertEqual(result["annotated"], True)
        self.assertEqual(result["is_disabled"], True)
        self.assertEqual(result["disabled_message"], "testlayer")
        self.assertEqual(result["data_url"], None)
        self.assertEqual(result["is_multilayer"], False)
        self.assertEqual(result["is_multilayer_parent"], False)
        self.assertEqual(result["dimensions"], [])
        self.assertEqual(result["associated_multilayers"], {})
        self.assertEqual(result["parent"], None)

class data_manager_get_json_test(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_view_api(self):
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
        Theme.objects.create(id=1, name="test", display_name="test", visible=True).site.set([1])
        Theme.objects.create(id=2, name="test2", display_name="test2", visible=True).site.set([1])

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
        theme1 = Theme.objects.create(id=1, name="test3", display_name="test3", visible=True, description="test 3")
        theme1.site.set([1])
        # Cannot use .set in the same line as creating an object as .set returns None
        theme2 = Theme.objects.create(id=2, name="test4", display_name="test4", visible=True, description="test 4")
        theme2.site.set([1])
        layer1 = Layer.objects.create(id=1, name="layertest1", is_sublayer=False)
        layer1.themes.set([theme1])
        layer2 = Layer.objects.create(id=2, name="layertest2", is_sublayer=True)
        layer2.sublayers.set([layer1])
        layer2.themes.set([theme1])
        layer3 = Layer.objects.create(id=3, name="layertest3", is_sublayer=False)
        layer3.themes.set([theme2])

     def test_get_layer_search_data_response_format(self):
        request = self.factory.get('/data_manager/get_layer_search_data')
        request.META['HTTP_HOST'] = "localhost:8000" 

        response = get_themes(request)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        print(result)


class DataManagerGetLayersForTheme(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()  

    def test_get_layer_search_data_response_format(self):
        request = self.factory.get('/data_manager/get_layer_search_data')
        request.META['HTTP_HOST'] = "localhost:8000" 

        response = get_themes(request)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)


      