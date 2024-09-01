from .forms import ApplicationForm, JobForm
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework.response import Response

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user)

class JobRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    def get_queryset(self):
        return Job.objects.filter(company=self.request.user)

class ApplicationListAPIView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        job_id = self.kwargs['job_id']
        return Application.objects.filter(job_id=job_id)

class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


class JobList(TemplateView):
    permission_classes = [IsAuthenticated]
    template_name = 'jobs/job_detail.html'
    def post(self, request):
        if request.user.is_company:
            return redirect('application-job-list')

class ListedJobs(TemplateView):
    permission_classed = [IsAuthenticated]
    template_name = 'jobs/job_c_list.html'


class JobApplyPage(TemplateView):
    template_name = 'jobs/job_apply.html'
    def post(self, request, job_id):
        job = get_object_or_404(Job, id=job_id)
        form = ApplicationForm()
        return render(request, 'jobs/job_apply.html', {
            'job': job,
            'form': form
        })
    
class CreateJobView(TemplateView):
    template_name = 'jobs/job_creation.html'
    def post(self, request):
        form = JobForm()
        return render(request, 'jobs/job_creation.html', {
            'form': form,
        })

class JobUpdateView(TemplateView):
    template_name = 'jobs/job_creation.html'
    def post(self, request, pk):
        form = JobForm()
        job = Job.objects.filter(id=pk)[0]
        return render(request, 'jobs/job_creation.html', {
            'form': form,
            'job': job,
        })
    
def delete_job(request, pk):
    if request.method == 'POST':
        job = Job.objects.filter(id=pk)
        job.delete()
        return redirect('jobs:application-job-list')

def list_applicants(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/single_job_applications.html', {
        'job': job,
    })

def job_apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.candidate = request.user
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('jobs:job-list')
        else:
            messages.error(request, 'There was an error with your application. Please try again.')
    else:
        form = ApplicationForm()
    
    return render(request, 'jobs/job_apply.html', {'form': form, 'job': job})