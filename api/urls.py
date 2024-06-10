from django.urls import path
from .views import *

urlpatterns = [
    
    path('summarize_text/', summarize_text, name='summarize-text'),
    
]
