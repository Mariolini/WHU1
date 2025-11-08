from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewUserRequest

class NewUserRequestListView(ListView):
    model = NewUserRequest
    template_name = "NURList.html"

class NewUserRequestDetailView(DetailView):
    model = NewUserRequest
    template_name = "NURDetail.html"

