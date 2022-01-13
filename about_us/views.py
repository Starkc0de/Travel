from django.views import generic
from django.shortcuts import render
from about_us.models import About_Us, Team_about


class AboutPage(generic.TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        about = About_Us.objects.all()
        About_team = Team_about.objects.all()
        page_name = "AboutUs"
        return render(request, self.template_name,{'about': about, 'About_team': About_team, 'page_name': page_name})
   