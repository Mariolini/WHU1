from django.urls import path
from .views import NewUserRequestListView, NewUserRequestDetailView, NewUserRequestCreateView, NewUserRequestUpdateView, NewUserRequestDeleteView

urlpatterns = [
    path("newuserrequest/new/", NewUserRequestCreateView.as_view(), name="NURnew"),
    path("newuserrequest/<int:pk>/", NewUserRequestDetailView.as_view(), name="NURDetail"),
    path("newuserrequest/<int:pk>/edit/", NewUserRequestUpdateView.as_view(), name="NURedit"),
    path("newuserrequest/<int:pk>/delete/", NewUserRequestDeleteView.as_view(), name="NURdelete"),
    path("", NewUserRequestListView.as_view(), name="NURList"),
]
