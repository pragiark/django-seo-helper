from django.shortcuts import render
from django.views import View
from .forms import AddClientForm


class AddClientView(View):
    template = 'django_seo_helper/add_client.html'

    def get(self, request):
        if request.method == "GET":
            form = AddClientForm(request.GET)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.save()
            # TODO create new template and return redirect to "detail" or sth

        # TODO: create file forms.py, define there form based on Model, then send form to template
        else:
            form = AddClientForm()
        return render(request, self.template, {'form': form})

            # TODO: in template - display for content by `form.as_p` e.g.

    def post(self, request):
        # TODO: when post send
        # TODO: redirect to same url when success and add message using django.contrib.messages.
        pass