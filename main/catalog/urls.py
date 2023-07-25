
from main.catalog.views import home, contacts, catalog
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from main.catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
        path('', home, name="home"),
        path('contacts/', contacts, name="contacts"),
        path("catalog/<int:pk>", catalog, name='catalog'),
    ]


