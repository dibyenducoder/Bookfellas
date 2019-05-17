from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .models import Book, Genre, Author, Profile
from .forms import UserForm

def book_detail(request,pk):
	book=get_object_or_404(Book,pk=pk)
	context={'book':book}
	return render(request,'books/book_detail.html',context)

def book_index(request):
	books=Book.objects.all()
	context={'books':books}
	return render(request,'books/book_index.html', context)

def author_detail(request,pk):
	author=get_object_or_404(Author,pk=pk)
	context={'author':author}
	return render(request,'books/author_detail.html',context)

def author_index(request):
	authors=Author.objects.all()
	context={'authors':authors}
	return render(request,'books/author_index.html', context)

def genre_detail(request,pk):
	genre=get_object_or_404(Genre,pk=pk)
	context={'genre':genre}
	return render(request,'books/genre_detail.html',context)

def genre_index(request):
	genres=Genre.objects.all()
	context={'genres':genres}
	return render(request,'books/genre_index.html', context)

def user_detail(request, pk):
    user=get_object_or_404(Profile,pk=pk)
    context ={'user':user}
    return render(request,'books/user_detail.html', context)
'''
def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect('user_detail',pk=user.pk)

    else:
        form=UserForm()
    return render(request, 'books/register.html', {'form': form})
'''

def register(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			user.save()
			user=authenticate(username=username, password= raw_password)
			login(request,user)
			return redirect('book_index')

	else:
		form=UserForm()
	return render(request, 'books/register.html', {'form': form})
