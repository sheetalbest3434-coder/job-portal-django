from django.shortcuts import render, redirect
from .models import Job

def home(request):
    return render(request, 'home.html')

def job_list(request):
    if request.method == "POST":
        Job.objects.create(
            title=request.POST['title'],
            company=request.POST['company'],
            location=request.POST['location'],
            salary=request.POST['salary']
        )
        return redirect('job_list')

    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})