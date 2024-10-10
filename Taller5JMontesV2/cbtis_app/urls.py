from django.urls import path,include # type: ignore
from cbtis_app import views

urlpatterns = [
    
    path('',views.listView,name='listView')
]