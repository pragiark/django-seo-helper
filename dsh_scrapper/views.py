from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import AddClientForm
from .models import Client, PageStatus


class AddClientView(View):
    template = 'django_seo_helper/add_client.html'

    def get(self, request):
        form = AddClientForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = AddClientForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
            messages.success(request, 'Added successfully')
            return redirect(reverse('add_client'))
        return render(request, self.template, {'form': form})


class ListClientView(View):
    template = 'django_seo_helper/list_client.html'

    def get(self, request):
        list_views = Client.objects.all()
        return render(request, self.template, {'list_views': list_views})


class ListScrape(View):
    template = 'django_seo_helper/scrapp_list.html'

    def get(self, request):
        scrapp_views = PageStatus.objects.all()
        return render(request, self.template, {'scrapp_views': scrapp_views})