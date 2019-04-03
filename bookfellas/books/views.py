from django.shortcuts import render, get_object_or_404
from .models import Book


def detail(request, pk):
    book=get_object_or_404(Book,pk=pk)
    context ={'book':book}
    return render(request,'books/detail.html', context)
