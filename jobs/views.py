from django.shortcuts import render, get_object_or_404

from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', context)

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    print(job_detail)
    context = {
        'job': job_detail,
    }
    return render(request, 'jobs/detail.html', context)
