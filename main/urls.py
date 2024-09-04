from .views import main_page
from django.urls import path, include


urlpatterns = [
   path('', main_page, name='main_page')
]

