from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from home.models import HomePageModel
from news.models import Blogpost
from destination.models import DestinationModel


class SearchViews(generic.TemplateView):
    template_name = "search.html"

    def get(self, request):
        if request.method == 'GET':
            query = request.GET.get('q')
            submitbutton = request.GET.get('submit')
            if query is not None:
                print(query)
                lookups = Q(destination_name__icontains=query) | Q(about_destination__icontains=query)
                blog = Q(title__icontains=query) | Q(blog__icontains=query) 
                desti = Q(place_name__icontains=query) | Q(about_place__icontains=query) 
                
                results = HomePageModel.objects.filter(lookups).distinct()
                blog_results = Blogpost.objects.filter(blog).distinct()
                Dest_results = DestinationModel.objects.filter(desti).distinct()

                print(results, blog_results,'gfdffhffhgfhfhfh')

                context = {'results': results, 'blog_results': blog_results,'data':Dest_results,
                           'submitbutton': submitbutton}
                

                return render(request, 'search.html', context)

            else:
                return render(request, 'search.html')

        else:
            return render(request, 'search.html')
