from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def sellers(request):
    return render(request,'top-sellers.html')
def login(requsets):
    return render(requsets,'advertisement-post.html')
def register(requests):
    return render(requests,'register.html')
def profile(requests):
    return render(requests,'profile.html')
def advertisement(requests):
    return render(requests,'advertisement.html')
def post(requests):
    return render(requests,'advertisement-post.html')