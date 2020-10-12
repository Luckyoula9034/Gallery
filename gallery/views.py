from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Article
from django.shortcuts import render
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def gallery_of_day(request):
    date = dt.date.today()
    return render(request, 'gallery/today-gallery.html')


def past_days_gallery(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    gallery = Article.days_gallery(date)
    return render(request, 'gallery/past-gallery.html', {"date": date,"gallery":gallery})

def gallery_today(request):
    date = dt.date.today()
    gallery = Article.todays_gallery()
    return render(request, 'gallery/today-gallery.html', {"date": date,"gallery":gallery})


def search_results(request):
    
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html', {"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})
    
    
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallery/article.html", {"article":article})    