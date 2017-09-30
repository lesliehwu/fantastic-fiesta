# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.db import connection, transaction

# Create your views here.

def index(request):
    context = {
            "users": User.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def edit(request, user_id):
    context = {
            "user":User.objects.get(id=user_id),
    }
    return render(request, 'edit.html', context)

def show(request, user_id):
    context = {
            "user":User.objects.get(id=user_id)
    }
    return render(request, 'show.html', context)

def create(request):
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
    return redirect('/users/')

def destroy(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/users/')

def update(request, user_id):
    user = User.objects.get(id=user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()
    return redirect('/users/')
