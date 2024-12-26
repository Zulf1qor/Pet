from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name="index_url"),
    path('about/', about_view, name="about_url"),
    path('service/', service_view, name="service_url"),
    path('blog/', blog_view, name="blog_url"),
    path('contact/', contact_view, name='contact_url'),
]