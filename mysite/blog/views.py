from django.shortcuts import render
from .models import Blog, Author, Entry

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    autors = Author.objects.all()
    entries = Entry.objects.all()
    data = {"blogs": blogs, 'autors': autors, 'entries': entries}
    return render(request, "blog/index.html", context=data)
