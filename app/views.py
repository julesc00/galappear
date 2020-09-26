from django.shortcuts import render


def index(request):
  context = {
    "title": "Galappear Theme",
    "page_title": "From Index Page"
  }

  return render(request, "app/index.html", context)
