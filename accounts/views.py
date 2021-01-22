from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
        
    context = {'form': form}

    
    return render(request, 'accounts/signup.html', context)

@login_required

def home(request):
    return render(request, 'accounts/home.html')