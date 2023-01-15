from django.shortcuts import render

# Create your views here.


def projectPage(request):

    # project = Project.objects.all()

    return render(
        request, 
        'project.html',
        {
            # 'projects': project
        }
        )