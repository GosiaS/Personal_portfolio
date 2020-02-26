from django.urls import path
from . import views
#from . views import add_to_cart, remove_from_cart

#app_name='mainstore'

urlpatterns = [
    path('', views.store_index, name='store_index')
]