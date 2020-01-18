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


class ListScrapeView(View):
    template = 'django_seo_helper/scraping_list.html'

    def get(self, request):
        scraping_views = PageStatus.objects.all()
        return render(request, self.template, {'scraping_views': scraping_views})
