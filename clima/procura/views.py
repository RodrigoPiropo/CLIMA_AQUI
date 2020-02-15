from django.shortcuts import render
import requests
from .models import Cidade
from .forms import CidadeForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d8ec2adac27c7bda8252c74338da9517'
    cidades = Cidade.objects.all()

    if request.method == 'POST':  # only true if form is submitted
        form = CidadeForm(request.POST)  # add actual request data to form for processing
        form.save()  # will validate and save if validate

    form = CidadeForm()
    dados_clima = []

    for cidade in cidades:
        clima_cidade = requests.get(url.format(cidade)).json()

        clima = {
            'cidade': cidade,
            'temperatura': clima_cidade['main']['temp'],
            'desc': clima_cidade['weather'][0]['description'],
            'icon': clima_cidade['weather'][0]['icon']
        }

        dados_clima.append(clima)

    context = {'dados_clima': dados_clima, 'form': form}

    return render(request, 'procura/index.html', context)
