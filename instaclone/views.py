from django.shortcuts import render

# Create your views here.
def newsfeed(request):
    return render(request, 'index.html')
