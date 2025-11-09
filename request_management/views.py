from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import NewUserRequest

class NewUserRequestListView(ListView):
    model = NewUserRequest
    template_name = "NURList.html"

class NewUserRequestDetailView(DetailView):
    model = NewUserRequest
    template_name = "NURDetail.html"

class  NewUserRequestCreateView(CreateView):
    model = NewUserRequest
    template_name = "NURnew.html"
    fields = ['requested_by',
              'for_firstname',
              'for_lastname',
              #'start_date',
              'campus',
              'department',
              'job_title',
              'office',
              'supervisor',
              'network_access',
              'mail_distribution_lists',
              'additional_email',
              'mystudies',
              'ac5',
              'moodle',
              'otrs'
              ]
    
class  NewUserRequestUpdateView(UpdateView):
    model = NewUserRequest
    template_name = "NURedit.html"
    fields = ['requested_by',
              'for_firstname',
              'for_lastname',
              #'start_date',
              'campus',
              'department',
              'job_title',
              'office',
              'supervisor',
              'network_access',
              'mail_distribution_lists',
              'additional_email',
              'mystudies',
              'ac5',
              'moodle',
              'otrs'
              ]
              
class NewUserRequestDeleteView(DeleteView):
    model = NewUserRequest
    template_name = "NURdelete.html"
    success_url = reverse_lazy("NURList")
