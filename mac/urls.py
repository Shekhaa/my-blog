from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/',admin.site.urls,name="admin"),
    path('',views.home,name="home"),
    path('about',views.about,name='about'),
    path('service',views.service,name="service"),
    path('shop/', include('shop.urls'))
]



