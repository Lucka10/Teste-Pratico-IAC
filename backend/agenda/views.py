from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from agenda.models import Contato

import json

def index(request):
    if request.method == 'GET':
        t = Contato.objects.all()
        response = []
        for i,_ in enumerate(t):
            data = {'id':t[i].id,'nome':t[i].nome,'email':t[i].email,'telefone':t[i].telefone,'date':t[i].datadenasc.isoformat()}
            print(f'DATA:{i}',data)
            response.append(data)
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse()

@csrf_exempt
def novo_contato(request):

    print(request)
    print('REQUEST:',request)
    print('METHOD:',request.method)
    print('BODY:',request.body)
    data = json.loads(request.body)
    print('DATA',data)


    if data.get('id'):
        editar = Contato.objects.filter(id=data.get('id'))
        print('Encontrei:',editar)
        editar = editar[0]
        editar.nome = data.get('nome')
        editar.email = data.get('email')
        editar.telefone = data.get('telefone')
        editar.datadenasc = data.get('date')
        editar.save()
        return HttpResponse('ALterei com SUCESSO')
     


    print('request:',data.get('nome')) 
    contato = Contato()
    contato.nome = data.get('nome')

    email=data.get('email')
    if email:
        contato.email = email

    telefone=data.get('telefone')
    if telefone:
        contato.telefone = telefone

    datadenasc=data.get('date')
    if datadenasc:
        contato.datadenasc = datadenasc
    #foto=data.get('foto')
    
    contato.save()
    print(contato)
    response = JsonResponse({'id':contato.id,'nome':contato.nome,'email':contato.email,'telefone':contato.telefone,'date':contato.datadenasc})
    response.status_code = 201
    return response


@csrf_exempt
def delete(request,id):
    print(request)
    print('ID:',id)
    print('REQUEST:',request)
    print('METHOD:',request.method)
    apagar = Contato.objects.filter(id=id)
    if apagar:
        nome = apagar[0].nome
        apagar.delete()
        if not Contato.objects.filter(id=id):
            response = HttpResponse(f'{nome} Removido com SUCESSO')
            response.status_code = 200
            return response