from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Reviews
from .forms import ReviewForm


@login_required
def review_create(request):

    reviews = Reviews.objects.order_by('-created_on')[:12]

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()

    else:
        form = ReviewForm()

    context = {'form': form,
               'reviews': reviews, }

    return render(request, 'reviews/review_form.html', context)
