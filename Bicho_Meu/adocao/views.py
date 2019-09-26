from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Adocao
from .models import Animal
from .models import Cliente
from .models import Doador
from .models import Raca


def index(request):
    registros = Adocao.objects.order_by('-registro')[:5]
    template = loader.get_template('adocao/index.html')
    context = {'registros': registros}
    return HttpResponse(template.render(context, request))


def adocao_detalhe(request, adocao_id):
    try:
        adocao = Adocao.objects.get(pk=adocao_id)
    except Adocao.DoesNotExist:
        raise Http404("Adoção não existe")
    return render(request, 'adocao/detalhe.html', {'adocao': adocao})


def clientes(request):
    registros = Cliente.objects.order_by('-registro')[:5]
    context = {'registros': registros, }
    return render(request, 'adocao/clientes.html', context)


def cliente_detalhe(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise Http404("Cliente não existe")
    return render(request, 'adocao/cliente_detalhe.html',
                  {'cliente': cliente})


def doadores(request):
    registros = Doador.objects.order_by('-registro')[:5]
    context = {'registros': registros, }
    return render(request, 'adocao/doadores.html', context)


def doador_detalhe(request, doador_id):
    doador = get_object_or_404(Doador, pk=doador_id)
    return render(request, 'adocao/doador_detalhe.html',
                  {'doador': doador})


def animais(request):
    registros = Animal.objects.order_by('-registro')[:5]
    context = {'registros': registros, }
    return render(request, 'adocao/animais.html', context)


def animal_detalhe(request, animal_id):
    try:
        animal = Animal.objects.get(pk=animal_id)
    except Animal.DoesNotExist:
        raise Http404("Animal não existe")
    return render(request, 'adocao/animal_detalhe.html',
                  {'animal': animal})


def racas(request):
    registros = Raca.objects.order_by('nome')
    context = {'registros': registros, }
    return render(request, 'adocao/racas.html', context)


def raca_detalhe(request, raca_id):
    raca = get_object_or_404(Raca, pk=raca_id)
    return render(request, 'adocao/raca_detalhe.html',
                  {'raca': raca})


def busca(request):
    context = {}
    if 'termo' in request.POST:
        termo = request.POST.get('termo', '')
        if len(termo) > 0:
            registros = Animal.objects.filter(nome=termo).order_by('nome')
            context['termo'] = termo
            context['registros'] = registros
        else:
            error_message = 'É necessário fornecer um termo de pesquisa!'
            context['termo'] = termo
            context['error_message'] = error_message

    return render(request, 'adocao/busca.html', context)
