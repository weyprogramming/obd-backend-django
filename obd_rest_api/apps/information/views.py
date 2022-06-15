from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="OBD REST API",
      default_version='v1',
      description="REST API to process data from the OBD-interface of different cars. Developed by the LAA from department 6 of FH Aachen",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="lennart.weyrowitz@alumni.fh-aachen.de"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)