
from django.urls import path
from . import views
from .views import RoomView
urlpatterns = [
    path('home',RoomView.as_view()),
    path('',views.index,name='index'),
]
