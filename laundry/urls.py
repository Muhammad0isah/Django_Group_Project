from django.urls import path
from django.contrib import admin

from .views import delivery, home, about, records, services, blog, contact, blog_detail, element

urlpatterns = [
    path("home/", home, name='home'),
    path("records/", records, name='records'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('blog/', blog, name="blog"),
    path('blog/blog_details/', blog_detail, name='details'),
    path('blog/elements/', element, name='elements'),
    path('contact/', contact, name='contact'),
    path('delivery/', delivery, name='delivery'),

]
