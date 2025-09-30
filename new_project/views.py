from django.shortcuts import render, get_object_or_404
from .models import New, Category, Contacts
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import New







def all_news(request):
    all_news = New.objects.filter(status=New.Status.PUBLISHED)
    context = {
        'news': all_news
    }
    return render(request, 'news/all.html', context)


def detail(request, pk):
    new = get_object_or_404(New, pk=pk, status=New.Status.PUBLISHED)
    context = {'new': new}
    return render(request, 'news/one.html', context)


def home_page_view(request):
    categories = Category.objects.all()
    news = New.objects.filter(status=New.Status.PUBLISHED) 
    last_uzb_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=9).order_by("-published_at")[0]
    uzb_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=9).order_by("-published_at")[1:]
    last_sport_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=7).order_by("-published_at")[0]
    sport_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=7).order_by("-published_at")[1:]
    last_fan_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=13).order_by("-published_at")[0]
    fan_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=13).order_by("-published_at")[1:]
    iqtisodiyot_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=10).order_by("-published_at")
    jahon_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=8).order_by("-published_at")
    last_moliya_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=11).order_by("-published_at")[0]
    moliya_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=11).order_by("-published_at")
    last_real_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=14).order_by("-published_at")[0]
    jamiyat_news = New.objects.select_related("category").filter(status=New.Status.PUBLISHED, category=12).order_by("-published_at")
    latest_news = New.objects.filter(status=New.Status.PUBLISHED).order_by("-created_at")[:8]


    print(uzb_news)
    context = {
        'categories': categories,
        'news': news,
        'last_uzb_news':last_uzb_news,
        'uzb_news':uzb_news,
        'last_sport_news':last_sport_news,
        'sport_news':sport_news,
        'last_fan_news':last_fan_news,
        'fan_news':fan_news,
        'iqtisodiyot_news':iqtisodiyot_news,
        'jahon_news':jahon_news,
        'moliya_news':moliya_news,
        'last_moliya_news':last_moliya_news,
        'last_real_news':last_real_news,
        'jamiyat_news':jamiyat_news,
        'latest_news': latest_news,
    }
    return render(request, 'news/home.html', context)


# def contact_us(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("Ma`lumotlaringiz muvaffaqiyatli yuborildi, Raxmat!\n\n<a href='/'>ASOSIY SAHIFA</a>")
#     context = {
#         'form':form
#     }
#     return render(request, 'news/contact.html', context)



class contact_us(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form':format
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method=="POST" and form.is_valid():
            form.save()
            return HttpResponse("Ma`lumotlaringiz muvaffaqiyatli yuborildi, Raxmat!\n\n<a href='/'>ASOSIY SAHIFA</a>")
        context = {
            'form':form
        }
        return render(request, 'news/contact.html', context)

def categories_list(request):
    categories = Category.objects.all()
    context ={
        'categories':categories
    }
    return render(request, 'news/categories.html', context)

def category_news(request, name):
    category = get_object_or_404(Category, name__iexact=name)
    category_news = New.objects.filter(category=category, status=New.Status.PUBLISHED)
    categories = Category.objects.all()
    context = {
        'category': category,
        'category_news': category_news,
        'categories': categories
    }
    return render(request, 'news/category_news.html', context)



def for_base_html(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context = {
        "categories":categories,
        "news":news
    }
    return render(request, 'news/base.html', context)
