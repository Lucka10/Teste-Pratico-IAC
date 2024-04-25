from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from agenda.models import Contato

import json

def index(request):
    t = Contato.objects.all()
    print(t[0])
    return HttpResponse(f"Hello, world. You're at the polls index. {t[0]}")

def Pegar_Contatos(request):
    if request.methos == 'GET':
        return HttpResponse("No Caminho")

@csrf_exempt
def novo_contato(request):
    data = json.loads(request.body.decode('utf-8'))
    print('REQUEST:',request)
    print('METHOD:',request.method)
    print('BODY:',request.body)
    print('DATA',data)
    print('METHOD:',request.content_params)
    print('request:',request.POST.get('nome')) 
    return HttpResponse(f"criou um novo contato {data}")