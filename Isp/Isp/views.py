from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
def home(request):
    return render (request,"home.html")

def main(request):
    return render (request,"main.html")

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('inicio'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context
    def get_success_url(self):
        success_url = reverse_lazy('inicio')
        print(f"Success URL: {success_url}")
        return success_url


class IndexView(TemplateView):
    template_name ='home.html'