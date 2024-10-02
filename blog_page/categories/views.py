from django.shortcuts import render,redirect
from .forms import CategoryrForm
# Create your views here.
def add_categories(request):
    if request.method == 'POST':
        category_form = CategoryrForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_categories')
    else:
        category_form = CategoryrForm()
        print('methdo post na')
    return render(request,'add_category.html',{'form':category_form})