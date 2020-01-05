from django.shortcuts import render
from django.views import View
from .forms import AddClientForm
from django.http import HttpResponseRedirect
from django.contrib import messages


class AddClientView(View):
    template = 'django_seo_helper/add_client.html'


    def get(self, request):
        # TODO: in template - display for content by `form.as_p` e.g.
        form = AddClientForm()
        return render(request, self.template, {'form': form})



    def post(self, request):
        # TODO: when post send
        form = AddClientForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
            # TODO: redirect to same url when success and add message using django.contrib.messages.
            messages.success(request, 'Udało się dodać')
            return render(request, self.template, {'form': form})
        pass