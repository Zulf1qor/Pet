from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *

def index_view(request):
    context = {
        'banner':Banner.objects.last(),
        'about': About.objects.last(),
        'advantages': Advantages.objects.all().order_by('-id')[:3],
        'service':Service.objects.all().order_by('-id')[:6],
        'choose':Choose.objects.last(),
        'advan': Advantages.objects.all().order_by('-id')[:4],
        'team':Team.objects.all().order_by('-id')[:4],
        'pricing':Pricing.objects.all().order_by('-id')[:3],

    }
    return render(request, 'index.html', context)

def about_view(request):
    context = {
        'about':About.objects.last(),
        'advantages':Advantages.objects.all().order_by('-id')[:3],
        'team': Team.objects.all().order_by('-id')[:4]


    }
    return render(request, 'about.html', context)


def service_view(request):
    context = {
        'service':Service.objects.all().order_by('-id')[:6]
    }
    return render(request, 'service.html', context)



def blog_view(request):
    # Fetch all blog posts, ordered by newest first
    blogs = Blog.objects.all().order_by('-id')

    # Set up the paginator (6 posts per page)
    paginator = Paginator(blogs, 6)

    # Get the current page number from the request query parameters
    page_number = request.GET.get('page', 1)  # Defaults to page 1

    # Get the Page object for the current page number
    page_obj = paginator.get_page(page_number)

    # Pass the Page object to the template
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog.html', context)



def single_view(request):
    context = {

    }
    return render(request, 'single.html', context)


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            surename=surname,
            subject=subject,
            message=message
        )
        return HttpResponse("Thank you for contacting us!")
    return render(request, 'contact.html')