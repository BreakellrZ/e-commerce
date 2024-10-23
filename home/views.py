from django.shortcuts import render
from faq.models import Faq
from django.contrib import messages
from faq.forms import QuestionForm

# Create your views here.


def index(request):
    """ A view to return index page along with reviews and faqs """

    faqs = Faq.objects.all()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            form = QuestionForm()
        messages.success(
            request, 'Your Question has been sent, please allow up to 24 hours for a reply. Thank you for contacting Paradise Pending')
    else:
        form = QuestionForm

    context = {'faqs': faqs,
               'form': form}
    return render(request, 'home/index.html', context)
