from django.contrib.auth.models import User
from django.shortcuts import render

from websiteapp.models import Movies, review


# Create your views here.
def review_page(request):
    id = request.GET.get('id')
    item_details = Movies.objects.get(id=id(id))
    user = request.session['email']
    user_detail = User.objects.get(email=user)
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        item_review = request.POST.get('item_review')

        item_reviews = review(user=user_detail, item=item_details, rating=star_rating, review_desp = item_review)
        item_reviews.save()

        rating_details = review.objects.filter(item=item_details)
        context = {'reviews': rating_details}
        return render(request, './websiteapp/review_page.html', context)

    rating_details = review.objects.filter(item=item_details)
    context = {'reviews': rating_details}
    return render(request, './reviewapp/review_page.html', context)