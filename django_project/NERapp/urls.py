# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.upload_view, name='upload'),
#     path('extracted/', views.extracted_view, name='extracted_info'),
# ]
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('api/process_pdf/', views.process_pdf, name='process_pdf'),
    # path('', views.upload_view, name='upload_view'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('', home, name='home'),
]