from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Rabbit
from .send import send
from .forms import AuthForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.core.urlresolvers import reverse
import uuid
import os


def index(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                instance = Rabbit(name=request.POST['name'],
                                  file=request.FILES['file'],
                                  user=request.user,
                                  guid=uuid.uuid4())
                instance.save()
                body = os.path.abspath(str(instance.file))
                send(body)
                print(body)
                return HttpResponseRedirect('success')
        else:
            form = UploadFileForm
        return render(request, 'rabbit_test/index.html', {'form': form})
    else:
        form = AuthForm()
        return render(request, 'rabbit_test/auth.html', {'form': form})


def success(request):
    return render(request, 'rabbit_test/success.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('rabbit_test:index'))
    else:
        form = UserCreationForm()
    return render(request, 'rabbit_test/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('rabbit_test:index'))
    else:
        form = AuthForm()
    return render(request, 'rabbit_test/auth.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('rabbit_test:index'))
