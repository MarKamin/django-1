from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import ArticleForm

# Create your views here.


def article_search_view(request):
    query = request.GET.get('q') # th is is a dictionary
    qs = Article.objects.search(query=query)
    context= {
        "object_list": qs
    }
    return render(request, "articles/search.html", 
    context=context)

@login_required
def article_create_view(request):
    #print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        return redirect("article-detail", slug=article_object.slug)
        #context['object'] = article_object
        #context['created'] = True
    return render(request, "articles/create.html", context=context)

def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.flter(slug=slug).first()
        except:
            raise Http404
    context = {
    "object": article_obj,

    }
    return render(request, "articles/detail.html", context=context)