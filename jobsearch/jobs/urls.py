from django.urls import path
from .views import JobListCreateAPIView,JobUpdateView,delete_job, JobRetrieveUpdateDestroyAPIView,CreateJobView, ApplicationListAPIView, JobList, list_applicants, ApplicationCreateView, job_apply, ListedJobs, JobApplyPage
from django.contrib.auth.decorators import login_required

app_name = 'jobs'

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('create_job/', CreateJobView.as_view(), name='create-job'),
    path('create_new_job/', JobListCreateAPIView.as_view(), name='create-new-job'),
    path('modify/<int:pk>/', JobUpdateView.as_view(), name='modify-job'),
    path('list_posted_jobs/', login_required(ListedJobs.as_view()), name='application-job-list'),
    path('list_jobs/', login_required(JobList.as_view()), name='job-list'),
    path('apply_job_page/<int:job_id>/', JobApplyPage.as_view(), name='job-apply-page'),
    path('apply_job/<int:job_id>/', job_apply, name='job-apply'),
    path('list_applicants/<int:job_id>/', list_applicants, name='applicants-list'),
    path('jobs/<int:pk>/', JobRetrieveUpdateDestroyAPIView.as_view(), name='job-retrieve-update-destroy'),
    path('jobs/<int:pk>/delete/', delete_job, name='job-delete'),
    path('jobs/<int:job_id>/applications/', ApplicationListAPIView.as_view(), name='application-list'),
]
