from django.views import generic
from django.shortcuts import render, get_object_or_404
from news.models import Blogpost
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# class BlogPage(generic.TemplateView,):
#     model = Blogpost
#     template_name = "news.html"
#     ordering = ['id']
#     paginate_by = 3
   
#     def get(self, request, *args, **kwargs):
#         blg = Blogpost.objects.all()
#         page_name = "news"
#         return render(request, self.template_name,{'blg': blg, 'page_name': page_name})

class BlogPage(ListView):
    model = Blogpost
    template_name = "news.html"
    paginate_by = 2

    def get_context_data(self, ** kwargs):
        context = super(BlogPage, self).get_context_data( ** kwargs)
        # blg = Blogpost.objects.all()
        blg = Blogpost.objects.all().order_by('id')
        page_name = "news"
        pagina = Paginator(blg, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = pagina.page(page)
        except PageNotAnInteger:
            file_exams = pagina.page(1)
        except EmptyPage:
            file_exams = pagina.page(pagina.num_pages)

        context['Blogpost'] = file_exams
        context['blg'] = blg
        context['page_name'] = page_name
        return context
        

class PostDetail(DetailView):
    model = Blogpost
    template_name = 'news.html'

    def get_context_data(self,request, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Blogpost, id=self.kwargs['id'])
        is_liked = False
        if post.likes.filter(id=request.user.id).exists():
            is_liked = True
        context["post"] = post
        context["is_liked"] = is_liked
        return context