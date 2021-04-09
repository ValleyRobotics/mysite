from django.shortcuts import render
from projects.models import Project, Image
#from projects.forms import ImageForm



def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)


# def showimage(request):
#     lastimage = Image.objects.last()
#
#     imagefile = lastimage.imagefile
#
#     form = ImageForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#
#     context = {'imagefile': imagefile,
#                'form': form
#                }
#
#     return render(request, 'Blog/images.html', context)