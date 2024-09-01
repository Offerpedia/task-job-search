from django.urls import path
from . import views 
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('register/company/', views.register_company, name='register_company'),
    path('register/candidate/', views.register_candidate, name='register_candidate'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('job_creation/', views.job_creation_view, name='job_creation'),  # Define this view in views.py
    # path('job_listing/', views.job_listing_view, name='job_listing'),  # Define this view in views.py
    # other URLs...
]
