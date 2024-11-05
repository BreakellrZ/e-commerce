from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Reviews
from .forms import ReviewForm


@login_required
def createReview(request):

    reviews = Reviews.objects.order_by('-created_on')[:12]

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(
                request, 'Your review has been created pending approval')
    else:
        form = ReviewForm()

    context = {'form': form,
               'reviews': reviews, }

    return render(request, 'reviews/review_form.html', context)


@login_required
def updateReview(request, pk):
    reviews = Reviews.objects.order_by('-created_on')[:12]
    review = Reviews.objects.get(id=pk)
    form = ReviewForm(instance=review)
    messages.success(
                request, 'EDIT YOUR REVIEW')

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid() and review.author == request.user:
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(
                request, 'Your review has been updated')
            return redirect('/')
        else:
            messages.error(
                request, ' ERROR: You must be the orginal author to edit this Review!')
            return redirect('/')

    context = {'form': form,
               'reviews': reviews}
    return render(request,  'reviews/review_form.html', context)


@login_required
def deleteReview(request, pk):
    review = Reviews.objects.get(id=pk)
    if request.method == "POST":
        review.delete()
        messages.success(
            request, 'Your review has been deleted')
        return redirect("/")
    context = {'item': review}
    return render(request, 'reviews/review_delete.html', context)

