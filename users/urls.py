from .api import UserAdmin,PF_admin,UserDatailsAdmin,PfDetailsAdmin
from django.urls import path
from rest_framework.documentation import include_docs_urls

###################################### NOTA IMPORTANTE ##########################################
#path('api/users/', include('users.urls')), ==> este es el path que precede las urls de users.urls
urlpatterns = [
    path('admin/', UserAdmin, name='user-admin'),
    path('pf/', PF_admin , name='pf-admin'),
    path('admin/<str:pk>/', UserDatailsAdmin , name='admin-user-details'),
    path('pf/<str:pk>/', PfDetailsAdmin , name='pf-user-details'),
    path('document/',include_docs_urls(title='documentacion')),
    path('docs/',include_docs_urls(title='document'))
]