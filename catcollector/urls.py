from django.contrib import admin
# Add the include function to the import
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
]