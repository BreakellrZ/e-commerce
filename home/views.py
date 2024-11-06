from django.shortcuts import render
from faq.models import Faq
from reviews.models import Reviews
from django.contrib import messages
from faq.forms import QuestionForm


# Create your views here.
def index(request):
    """ A view to display Home page along with reviews and faqs """

    # Get all faqs from Faq model and the most recent 6 reviews
    faqs = Faq.objects.all()
    reviews = Reviews.objects.order_by('-created_on')[:7]

    # Contact us Form
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            form = QuestionForm()
        messages.success(
            request, 'Your Question has been sent, please allow up to 24 hours for a reply. Thank you for contacting Paradise Pending')
    else:
        form = QuestionForm()

    context = {'faqs': faqs,
               'reviews': reviews,
               'form': form}
    return render(request, 'home/index.html', context)
