from django.conf.urls import url, include, patterns
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'layers', views.LayerViewSet)

urlpatterns = patterns('',
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^api/', include(router.urls)),
    (r'^layer/([A-Za-z0-9_-]+)$', views.update_layer),
    (r'^layer$', views.create_layer),
    (r'^get_json$', views.get_json),
    (r'^get_themes$', views.get_themes),
    (r'^get_layer_search_data$', views.get_layer_search_data),
    (r'^get_layers_for_theme/(?P<themeID>\d+)$', views.get_layers_for_theme),
    (r'^get_layer_details/(?P<layerID>\d+)$', views.get_layer_details),
    (r'^wms_capabilities', views.wms_request_capabilities),
)
