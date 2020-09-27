from django.shortcuts import render


def index(request):
    context = {
        "title": "Cari's Site",
        "page_title": "From Index Page"
    }

    return render(request, "app/index.html", context)


def gaming_view(request):
    context = {}
    return render(request, "app/gaming.html", context)


def logos_view(request):
    context = {}
    return render(request, "app/logos.html", context)
