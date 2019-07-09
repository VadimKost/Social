from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .form import *


# Create your views here.
@login_required(login_url='Auth/')
def User_View(request):
    name = auth.get_user(request).username
    if request.method == 'POST':
        auth.logout(request)
    return render(request, 'User.html', locals())


def Mesage1(request):
    user = auth.get_user(request)
    Mesagelist = Message.objects.filter(sen=user)

    return render(request, 'Mesage.html', locals())


def reg(request):
    form = UserCreationForm()
    if request.method == 'POST':
        new_form = UserCreationForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            aut = auth.authenticate(username=new_form.cleaned_data['username'],
                                    password=new_form.cleaned_data['password2'])
            auth.login(request, aut)
            return redirect('/')
    return render(request, 'Reg.html', locals())


def Auth(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    return render(request, 'Auth.html', locals())


def Dialog_view(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    user_id = request.user.id
    return render(request, 'Dialog.html', locals())


def Dialog(request, dialog_id):
    user = auth.get_user(request)
    chat = Chat.objects.get(id=dialog_id)
    msg = Message.objects.filter(chat=dialog_id)
    form = MessageForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        message = form.save(commit=False)
        message.chat_id = dialog_id
        message.autor = request.user
        message.save()
        return redirect(request.path)

    return render(request, 'Mesage.html', locals())
