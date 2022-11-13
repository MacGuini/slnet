import os

from django.shortcuts import render, redirect
from .models import Job, Application
from django.template import context
from .forms import ApplicationForm, ReviewAppForm, JobForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def jobBoard(request):
    jobs = Job.objects.all()

    context = {'jobs':jobs}
    return render(request, 'careers/job_board.html', context)

@login_required(login_url='login')
def postJob(request):
    form = JobForm()

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job-board')

    context = {'form':form}
    return render(request, 'careers/post_job.html',context)

@login_required(login_url='login')
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('job-board')
    context = {'object':job}
    return render(request, "delete_template.html", context)

@login_required(login_url='login')
def updateJob(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job-board')
    context = {'form':form}
    return render (request,'careers/update_job.html', context)

@login_required(login_url='login')
def jobAppList(request):
    fields = Application.objects.all()

    context = {'fields':fields}
    return render(request, 'careers/job_app_list.html', context)

@login_required(login_url='login')
def viewJobApp(request, pk):
    app = Application.objects.get(id=pk)
    form = ReviewAppForm(instance = app)
    
    if request.method == 'POST':
        form = ReviewAppForm(request.POST, request.FILES, instance=app)
        
        if form.is_valid():
            form.save()

            return redirect('job-app-list')


    context = {'form':form, 'app':app}

    return render(request, 'careers/view_job_app.html', context)

@login_required(login_url='login')
def deleteJobApp(request, pk):
    app = Application.objects.get(id=pk)

    if request.method == 'POST':

        app.delete()

        
        return redirect('job-app-list')
    context = {'object':app}
    return render (request, 'delete_template.html', context)



def applyJob(request, jobId):
    form = ApplicationForm()
    job = Job.objects.get(id=jobId)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            
            application.save()

            return redirect ('job-board')

    context = {'form':form, 'job':job,}
    return render (request, 'careers/job_app.html', context)
