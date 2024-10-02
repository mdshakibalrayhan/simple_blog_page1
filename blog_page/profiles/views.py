# views.py
from django.shortcuts import render, redirect
from .forms import ProfileForm

def add_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_profile')  # Redirect to a success page
    else:
        form = ProfileForm()
    
    return render(request, 'add_profile.html', {'form': form})
