from django.shortcuts import render
from faq.models import Faq

# Create your views here.


def index(request):
    """ A view to return index page """

    faqs = Faq.objects.all()

    context = {'faqs': faqs, }
    return render(request, 'home/index.html', context)
