from django.urls import path
from django.urls.conf import include
from rest_framework import routers                   
from .views import MesaView,DataRelevanteView

routerData = routers.DefaultRouter()

routerData.register(r'mesa',MesaView)
routerData.register(r'data_relevante',DataRelevanteView)


urlpatterns = [
	path('',include(routerData.urls))
]