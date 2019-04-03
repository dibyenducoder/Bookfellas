from django.shortcuts import render, get_object_or_404
from .models import Author

def detail(request, pk):
    author=get_object_or_404(Author,pk=pk)
    context ={'author':author}
    return render(request,'authors/detail.html', context)
