import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('search_jobs')  # Redirect to the job search page after signup
    else:
        form = SignupForm()
    return render(request, 'jobs/signup.html', {'form': form})

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('search_jobs')  # Redirect to the job search page after login
    else:
        form = LoginForm()
    return render(request, 'jobs/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required  # Require the user to be logged in to access this view
def search_jobs(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        location = request.POST.get('location')
        date_since_posted = request.POST.get('dateSincePosted')
        job_type = request.POST.get('job_type')
        remote_filter = request.POST.get('remoteFilter')
        salary = request.POST.get('salary')
        experience_level = request.POST.get('experienceLevel')
        limit = request.POST.get('limit')
        sort_by = request.POST.get('sortBy')
        page = request.POST.get('page')

        # Define payload for Node.js API
        payload = {
            "keyword": keyword,
            "location": location,
            "dateSincePosted": date_since_posted,
            "jobType": job_type,
            "remoteFilter": remote_filter,
            "salary": salary,
            "experienceLevel": experience_level,
            "limit": "10",
            "sortBy": sort_by,
            "page": "0"
        }

        # Make request to Node.js server
        try:
            response = requests.post('http://localhost:3000/search-jobs', json=payload)
            jobs = response.json()  # Get jobs from the response
        except requests.exceptions.RequestException:
            jobs = []  # Handle errors gracefully

        return render(request, 'jobs/job_results.html', {'jobs': jobs})

    return render(request, 'jobs/search.html')
