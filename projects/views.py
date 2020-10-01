from django.shortcuts import render,get_object_or_404
from .models import Project
from accounts.models import EmployeeProfile


def project_list_view(request):
    """
    * Show all projects.
    """
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, 'projects/list.html', context)


def project_detail_view(request, id):
    """
    * Show details of a single project.
    @param id - id of the project
    """
    project = get_object_or_404(Project, pk=id)
    team_members = EmployeeProfile.objects.filter(team=project.team_alloted)
    context = {
        "project" : project,
        "team_members" : team_members
    }
    return render(request, 'projects/details.html', context)