from django.shortcuts import render
from django.views import generic
from services.models import ServiceModel

# Create your views here.

class Service(generic.TemplateView):
    template_name = "services.html"

    def get(self, request, *args, **kwargs):
        srv = ServiceModel.objects.all()
        page_name = "services"
        return render(request, self.template_name, { 'srv': srv, 'page_name': page_name})
