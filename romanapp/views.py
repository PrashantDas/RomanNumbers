from django.shortcuts import render
from .forms import DataForm
from .RomanNumerals import starter

# Create your views here.

def home(request):
    if request.method == 'POST':
        my_form = DataForm(request.POST)
        if my_form.is_valid():
            num = my_form.cleaned_data.get('number')
            result = starter(num)
            return render(request, 'romanapp/home.html', {'result': result, 'data_form': DataForm(request.POST)})
        else:
            return render(request, 'romanapp/home.html', {'data_form': DataForm()})
    else:
        return render(request, 'romanapp/home.html', {'data_form': DataForm()})

def contact(request):
    return render(request, 'romanapp/contact.html', {})