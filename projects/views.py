from django.shortcuts import render
from .models import Project

# Create your views here.


def projectPage(request):

    projects = Project.objects.all()

    # for project in projects:
    #     stack_list_str = project.stacks
    #     stacks_list = stack_list_str.split(",") if stack_list_str else []

    return render(
        request, 
        'project.html',
        {
            'projects': projects,
            # 'stacks': stacks_list
        }
        )