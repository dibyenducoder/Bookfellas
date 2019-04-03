from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

def detail(request, pk):
    user=get_object_or_404(User,pk=pk)
    context ={'user':user}
    return render(request,'users/detail.html', context)

def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            return redirect('detail',pk=user.pk)

    else:
        form=UserForm()
    return render(request, 'users/register.html', {'form': form})