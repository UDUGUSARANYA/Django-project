# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('recruiter/dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
#     path('jobseeker/dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
#     path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('application/<int:app_id>/<str:status>/', views.update_application_status, name='update_application_status'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('dashboard/', views.redirect_dashboard, name='dashboard'),


]
