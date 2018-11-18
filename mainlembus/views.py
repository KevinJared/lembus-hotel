from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime as dt


def index(request):
    date = dt.date.today()
    return render(request, 'index.html',{"date": date})
