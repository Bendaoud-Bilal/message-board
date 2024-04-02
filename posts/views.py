# posts/views.py
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


# for superuser : bilo - bendaoudbilal717@gmail.com - BILO123bend
