from django.shortcuts import render
from .models import Post, User
import datetime
def index(request):
    author = User.objects.get(username='leo')
    keyword = "утро"
    posts = None
    start_date = datetime.date(1854, 7, 7)
    end_date = datetime.date(1854, 7, 21)
    #posts = Post.objects.all()
    posts = Post.objects.filter(text__contains=keyword).filter(author=author).filter(pub_date__range=(start_date, end_date))
    return render(request, "index.html", {"posts": posts})
