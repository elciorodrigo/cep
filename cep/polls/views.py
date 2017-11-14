# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

import requests


def index(request):
    return render(request, 'polls/index.html')

def detail(request, cep):
    req = 'https://viacep.com.br/ws/' + cep + '/json/'
    response = requests.get(req)

    if(response.status_code!=200):
        data = {'erro' : "consulta não retornou resultados"}
    else:
        data = {'bairro': response.json().get("bairro"),
                'logradouro': response.json().get("logradouro"),
                'localidade': response.json().get("localidade"),
                'cep': response.json().get("cep")}
    return render(request, 'polls/detail.html', data)

