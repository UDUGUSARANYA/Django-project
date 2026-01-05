from django.shortcuts import render, redirect
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'jobs': jobs})



@login_required
def recruiter_dashboard(request):
    jobs = Job.objects.filter(recruiter=request.user)
    applications = Application.objects.filter(job__recruiter=request.user)
    return render(request, 'recruiter_dashboard.html', {
        'jobs': jobs,
        'applications': applications
    })


@login_required
def jobseeker_dashboard(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'jobseeker_dashboard.html', {'applications': applications})


# @login_required
# def apply_job(request, job_id):
#     if request.method == 'POST':
#         job = Job.objects.get(id=job_id)
#         resume = request.FILES['resume']
#         Application.objects.create(
#             job=job,
#             applicant=request.user,
#             resume=resume
#         )
#         return redirect('jobseeker_dashboard')
#     return render(request, 'apply_job.html', {'job_id': job_id})
@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    # Prevent duplicate application
    if Application.objects.filter(job=job, applicant=request.user).exists():
        return render(request, 'apply_job.html', {
            'job': job,
            'error': 'You have already applied for this job.'
        })

    if request.method == 'POST':
        resume = request.FILES['resume']
        Application.objects.create(
            job=job,
            applicant=request.user,
            resume=resume
        )
        return redirect('jobseeker_dashboard')

    return render(request, 'apply_job.html', {'job': job})
@login_required
def update_application_status(request, app_id, status):
    application = Application.objects.get(id=app_id)
    application.status = status
    application.save()
    return redirect('recruiter_dashboard')
from django.contrib.auth.models import Group

@login_required
def redirect_dashboard(request):
    if request.user.groups.filter(name='Recruiter').exists():
        return redirect('recruiter_dashboard')
    else:
        return redirect('jobseeker_dashboard')




