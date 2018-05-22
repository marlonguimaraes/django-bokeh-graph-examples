from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('plot', views.plot, name='plot'),
    path('vbar', views.vbar, name='bar'),
]