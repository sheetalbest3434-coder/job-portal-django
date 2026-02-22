from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Job

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_staff or user.is_superuser:
                login(request, user)
                messages.success(request, 'Login successful! Welcome Admin.')
                return redirect('admin_jobs')
            else:
                messages.error(request, '❌ Only admins can access the admin panel!')
                return redirect('login')
        else:
            messages.error(request, '❌ Invalid username or password!')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def is_admin(user):
    """Check if user is admin/staff"""
    return user.is_staff or user.is_superuser

# Public view - Everyone can see jobs
def jobs_view(request):
    jobs = Job.objects.all().order_by('-id')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    location_filter = request.GET.get('location', '')
    
    if search_query:
        jobs = jobs.filter(
            title__icontains=search_query
        ) | jobs.filter(company__icontains=search_query)
    
    if location_filter:
        jobs = jobs.filter(location__icontains=location_filter)
    
    # Get unique locations for filter
    locations = Job.objects.values_list('location', flat=True).distinct()
    
    context = {
        'jobs': jobs,
        'locations': locations,
        'search_query': search_query,
        'location_filter': location_filter,
    }
    return render(request, 'jobs/jobs_list.html', context)

# Admin only - Can post jobs (CREATE)
@login_required(login_url='login')
def admin_jobs(request):
    # Extra security check - if not admin, deny access
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, '🔐 Unauthorized! Only admins can access this page.')
        return redirect('home')
    
    if request.method == "POST":
        # Double check that only admin can post
        if not (request.user.is_staff or request.user.is_superuser):
            return HttpResponseForbidden('You do not have permission to post jobs.')
        
        Job.objects.create(
            title=request.POST.get('title', ''),
            company=request.POST.get('company', ''),
            location=request.POST.get('location', ''),
            salary=request.POST.get('salary', ''),
            description=request.POST.get('description', '')
        )
        messages.success(request, '✅ Job posted successfully!')
        return redirect('admin_jobs')

    jobs = Job.objects.all().order_by('-id')
    return render(request, 'jobs/admin_jobs.html', {'jobs': jobs})

# Admin only - UPDATE/Edit job
@login_required(login_url='login')
def edit_job(request, job_id):
    # Security check - only admin
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, '🔐 Unauthorized! Only admins can edit jobs.')
        return redirect('home')
    
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        messages.error(request, '❌ Job not found!')
        return redirect('admin_jobs')
    
    if request.method == "POST":
        job.title = request.POST.get('title', job.title)
        job.company = request.POST.get('company', job.company)
        job.location = request.POST.get('location', job.location)
        job.salary = request.POST.get('salary', job.salary)
        job.description = request.POST.get('description', job.description)
        job.save()
        messages.success(request, '✅ Job updated successfully!')
        return redirect('admin_jobs')
    
    return render(request, 'jobs/edit_job.html', {'job': job})

# Admin only - DELETE job
@login_required(login_url='login')
def delete_job(request, job_id):
    # Security check - only admin
    if not (request.user.is_staff or request.user.is_superuser):
        messages.error(request, '🔐 Unauthorized! Only admins can delete jobs.')
        return redirect('home')
    
    try:
        job = Job.objects.get(id=job_id)
        job_title = job.title
        job.delete()
        messages.success(request, f'✅ Job "{job_title}" deleted successfully!')
    except Job.DoesNotExist:
        messages.error(request, '❌ Job not found!')
    
    return redirect('admin_jobs')