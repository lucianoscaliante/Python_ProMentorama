from django.shortcuts import render

from .models import Filmes


# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name="home.html",
        context={"Titulo_filmes": Filmes.objects.all}
    )
