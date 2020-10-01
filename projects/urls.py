from django.urls import path
from .views import project_list_view, project_detail_view

app_name = "projects"
urlpatterns = [
    path('', project_list_view, name="list"),
    path('<int:id>/details/', project_detail_view, name="details"),
]