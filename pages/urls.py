from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from pages.views import index, ajax
 
urlpatterns = [
    #path('', HomePageView.as_view(), name='index'),
    path('', views.index, name='index'),
    url(r'^ajax/', views.ajax, name='ajax'),
]