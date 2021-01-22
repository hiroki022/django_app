from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        context = {'form': form}
        
        if form.is_valid():
            form.save()
            return redirect('accounts/login.html')
    else:
        form = SignUpForm()

    
    return render(request, 'accounts/signup.html', context)

@login_required

def home(request):
    return render(request, 'accounts/home.html')