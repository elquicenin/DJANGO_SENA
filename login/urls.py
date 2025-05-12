from .api import LoginAdmin, LoginEmpresa
from django.urls import path

#path('api/login/', include('login.urls')), ==> este es el path que precede las urls de users.urls

urlpatterns = [
    path("adminlog", LoginAdmin),
    path("loginempresa", LoginEmpresa),
]
