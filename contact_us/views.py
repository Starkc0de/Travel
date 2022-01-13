from django.shortcuts import render
from django.views import generic
from contact_us.forms import contact_us_Form

# Create your views here.


class ContactCreateView(generic.edit.CreateView):
    template_name = "contact.html"
    form_class = contact_us_Form
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['page_name'] = "ContactUs"
        return context
