from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('jobs/', views.jobs_view, name='jobs'),  # Public jobs view (READ)
    path('admin/jobs/', views.admin_jobs, name='admin_jobs'),  # Admin only - CREATE
    path('admin/jobs/edit/<int:job_id>/', views.edit_job, name='edit_job'),  # UPDATE
    path('admin/jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),  # DELETE
]