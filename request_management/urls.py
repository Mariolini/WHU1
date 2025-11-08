from django.urls import path
from .views import NewUserRequestListView, NewUserRequestDetailView

urlpatterns = [
    path("newuserrequest/<int:pk>/", NewUserRequestDetailView.as_view(), name="NURDetail"),
    path("", NewUserRequestListView.as_view(), name="NURList"),
]
