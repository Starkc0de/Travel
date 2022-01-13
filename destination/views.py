from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic
from home.models import HomePageModel

# Create your views here.

class DestinationView(generic.TemplateView):
    template_name = "destinations.html"

    def get(self, request, id, slug, *args, **kwargs):
        destination_data = None

        if HomePageModel.objects.filter(slug=slug).filter(id=id).exists():
            destination_data = get_object_or_404(
                HomePageModel, slug=slug, id=id)

        return render(request, self.template_name, {'destination_data': destination_data})
