from django.shortcuts import render

# Create your views here.
def newsfeed(request):
    return render(request, 'newsfeed.html')


def newsfeed_images(request):
    return render(request, 'newsfeed-images.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'timeline.html')


def profile_about(request):
    return render(request, 'timeline-about.html')