from django.urls import path
from .views import signup, welcome, login
from laundry.views import home

urlpatterns = [
    path('laundry/', home),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
