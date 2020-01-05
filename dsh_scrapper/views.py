from django.contrib import messages
from django.shortcuts import render
from django.views import View

from .forms import AddClientForm


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
            messages.success(request, 'Udało się dodać')
            # TODO: redirect to same url when success and add message using django.contrib.messages.
            return render(request, self.template, {'form': form})
        return render(request, self.template, {'form': form})
