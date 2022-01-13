from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


class AccountsView(generic.TemplateView):
    template_name = "accounts.html"

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return render(request, self.template_name)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return render(request, self.template_name)
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'User signned in.')
                return render(request, self.template_name)
        else:
            messages.info(request, 'Password does not match')
        return render(request, self.template_name)


class SigninView(generic.TemplateView):
    template_name = "signin.html"

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(1235646)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User Logged In')
            return HttpResponseRedirect(reverse('accounts:Account'))

        else:
            messages.info(request, 'Invalid User')
            return render(request, self.template_name)
