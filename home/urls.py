
from django.urls import path
from home.views import home
# from . import views

urlpatterns = [
    path('main/',home)  

]
