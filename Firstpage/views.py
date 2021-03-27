from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'Firstpage/home.html' )

@login_required
def current_todo(request):
    todos=Todo.objects.filter(user=request.user, completed__isnull=True)
    return render(request, 'Firstpage/current_todo.html', {'todos':todos })

@login_required
def viewtodo(request,todo_pk):
    todo=get_object_or_404(Todo,pk=todo_pk, user=request.user)
    if(request.method=='GET'):
        form=TodoForm(instance=todo)
        return render(request, 'Firstpage/detail_todo.html', {'todo':todo, 'form':form })
    else:
        form=TodoForm(request.POST, instance=todo)
        form.save()
        return redirect('current_todo')

def signin(request):
    if(request.method=='GET'): #when the page is reloaded and come to this page
        return render(request, 'Firstpage/signin.html', { 'form':AuthenticationForm()} )
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        #user=authenticate(request, usernanme=='aa', password=='aa')
        if(user is None):
            return render(request, 'Firstpage/signin.html', {'form':AuthenticationForm(), 'message':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('current_todo')
def signup(request):
    if(request.method=='GET'): #when the page is reloaded and come to this page
        return render(request, 'Firstpage/signup.html', { 'form':UserCreationForm()} )
    else:

        if(request.POST['password1'] == request.POST['password2']):  #when we hit the submit button check both the passwords are same
            try:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)   #after signup we have to keep that user logged in and transfer to the new page
                return redirect('current_todo')
            except IntegrityError:             #This is use to handle when username is already registered
                return render(request, 'Firstpage/signup.html', { 'form':UserCreationForm(), 'message':'This username is already taken please choose another one.' } ) #Here we are passing the error message when password did not same as confirm pass
        else:
                return render(request, 'Firstpage/signup.html', { 'form':UserCreationForm(), 'message':'Password did not matach' } ) #Here we are passing the error message when password did not same as confirm pass
@login_required
def create_todo(request):
    if(request.method=='GET'):
        return render(request, 'Firstpage/create_todo.html', {'form':TodoForm()})
    else:
        try:
            form=TodoForm(request.POST)   #here we are getting the form info
            newtodo=form.save(commit=False)
            newtodo.user= request.user
            newtodo.save()
            return redirect('current_todo')
        except(valueError):
            return render(request, 'Firstpage/create_todo.html', {'form':TodoForm(), 'message':'data is incorrect'})
@login_required
def completed(request,todo_pk):
    todo=get_object_or_404(Todo,pk=todo_pk, user=request.user)   #captring the the particcular todo
    if(request.method=='POST'):
        todo.completed=timezone.now()  #here we are setting the date completed and so when we set this date it will show as completed
        todo.save()
        return redirect('current_todo')
@login_required
def delete(request,todo_pk):
    todo=get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if(request.method=='POST'):
        todo.delete()
        return redirect('current_todo')
@login_required
def completed_todos(request):
    todos=Todo.objects.filter(user=request.user, completed__isnull=False).order_by('-completed')
    return render(request, 'Firstpage/completed_todos.html', {'todos':todos })
@login_required
def logoutuser(request):
    if(request.method=="POST"):
        logout(request)
        return redirect( 'home')
