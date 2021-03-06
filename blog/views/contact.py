from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import ContactForm
from blog.models import Contact


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context=context)
