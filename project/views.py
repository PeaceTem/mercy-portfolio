from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView


from .models import Project


class HomePage(TemplateView):
    template_name="project/homepage.html"

    def get(self, request, *args, **kwargs):
        # get the sequence and spits out the output
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.all()
        return context
    


# create a detail page to show the details of each project.

class DetailPage(DetailView):
    model = Project
    template_name = 'project/detailpage.html'  # Template file to be rendered
    context_object_name = 'project'  # Name to refer to the object in the template