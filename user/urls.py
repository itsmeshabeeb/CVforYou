from django.urls import path
from .import views

urlpatterns = [
    path("index",views.index, name="index"),
    path('master',views.index1,name='master'),
    path("templates",views.templateFun,name="templates"),
    path("personal",views.personal,name="Personal"),
    path('experiences',views.experiences,name="experiences")
    
]