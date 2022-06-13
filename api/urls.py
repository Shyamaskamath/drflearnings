from django.urls import path
from . import views
urlpatterns = [
    path('',views.CreateView.as_view(),name="create/view"),
    path('<int:pk>/',views.UpdatedeleteRetrive.as_view(),name="updte/delete/reterive")
   
]