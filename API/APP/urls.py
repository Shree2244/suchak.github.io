# APP/urls.py

# from django.urls import path
# from .views import ExtractEntitiesView

# urlpatterns = [
#     path('extract_entities/', ExtractEntitiesView.as_view(), name='extract_entities'),
# ]

from django.urls import path
from .views import process_pdf  # Ensure this imports the correct view

urlpatterns = [
    path('process_pdf/', process_pdf, name='process_pdf'),  # Adjust this if necessary
]