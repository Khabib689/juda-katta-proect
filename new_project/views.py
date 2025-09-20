from django.shortcuts import render, get_object_or_404
from .models import New, Category, Contacts
from .forms import ContactForm
from django.http import HttpResponse
from django.views.generic import TemplateView




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
    context = {
        'categories': categories,
        'news': news
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




