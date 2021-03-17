from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        'title': 'this is about us',
        'my_number': 123,
        'my_list': ['One', 21, 'Two', 'Three']
    }
    return render(request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})
