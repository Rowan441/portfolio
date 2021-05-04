from django.shortcuts import render, get_object_or_404

from .models import Job, Topic

# Create your views here.
def home(request):
    jobs = Job.objects
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', context)

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    context = {
        'job': job_detail,
    }
    return render(request, 'jobs/detail.html', context)

def topicdetail(request, topic_id):
    topic_detail = get_object_or_404(Topic, pk=topic_id)
    print(topic_detail.jobs.all())
    context = {
        'topic': topic_detail,
    }
    return render(request, 'jobs/topicdetail.html', context)