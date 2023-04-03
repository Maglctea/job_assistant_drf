from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from landingapp.forms import AddUserForm


class RegisterUser(CreateView):
    form_class = AddUserForm
    template_name = 'landingapp/index.html'
    success_url = reverse_lazy('add-user')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_name'] = 'Регистрация'
    #     return context
    #
    # def form_valid(self, form):
    #     user = form.save()
    #     return redirect('dashboard')


def error404(request, exception):
    return render(request, 'landingapp/404.html')
