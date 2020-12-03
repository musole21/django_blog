from django.urls import path
from . import views as blog_views

app_name = 'blog'
urlpatterns = [
    path('', blog_views.index, name='home'),
    path('about/', blog_views.about, name='about')
]
