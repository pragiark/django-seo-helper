from django.shortcuts import render
from django.views import View
from .forms import AddClientForm

class AddClientView(View):
    template = 'django_seo_helper/add_client.html'

    def get(self, request):
        # TODO: create file forms.py, define there form based on Model, then send form to template
        form = AddClientForm()
        # TODO: in template - display for content by `form.as_p` e.g.
        return render(request, self.template)

    def post(self, request):
        # TODO: when post send
        # TODO: redirect to same url when success and add message using django.contrib.messages.
        pass
