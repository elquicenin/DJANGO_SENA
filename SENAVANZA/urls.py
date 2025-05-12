"""
URL configuration for SENAVANZA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularSwaggerView,
#     SpectacularRedocView,
# )
# from myapp.views import saludo
# from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # y le include lo que hace es acceder a las rutas que se encuentran en 'myapp'
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')),
    path('api/login/',include('login.urls')),
    
    
#     # Genera el esquema OpenAPI en formato JSON
#     path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

#     # Documentación Swagger UI
#     path("api/docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

#     # Documentación ReDoc
#     path("api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ]
