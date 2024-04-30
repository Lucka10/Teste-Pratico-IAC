from django.http import HttpResponse,JsonResponse,FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from agenda.models import Contato

from PIL import Image

import json

@csrf_exempt
def index(request,id=None):
    if request.method == 'GET':
        t = Contato.objects.all()
        response = []
        for i,_ in enumerate(t):
            data = {'id':t[i].id,'nome':t[i].nome,'email':t[i].email,'telefone':t[i].telefone,'date':t[i].datadenasc.isoformat(),'foto':t[i].foto.url}
            print(f'DATA:{i}',data)
            response.append(data)
        return JsonResponse(response, safe=False)
    
    elif request.method == 'POST':
#        print(request)
#        print('REQUEST:',request)
#        print('METHOD:',request.method)
#       print('BODY:',request.body)
#        print('POST',request.POST)
#       print('FILE:',request.FILES)

        
        data = request.POST

        print(data)
        print('DATA',data)
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
       
        
        contato.save()
        if request.FILES:
            contato.foto=request.FILES['foto']
            contato.save()
        print(contato)
        response = JsonResponse({'id':contato.id,'nome':contato.nome,'email':contato.email,'telefone':contato.telefone,'date':contato.datadenasc,'foto':contato.foto.url})
        response.status_code = 201
        return response
    
    elif request.method == 'PUT':
#        print(request)
#        print('REQUEST:',request)
#        print('METHOD:',request.method)
#        print('HEAD:',request.headers)
#        print('BODY:',request.body)
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
        
    elif request.method == 'DELETE':
#        print(request)
#        print('ID:',id)
#        print('REQUEST:',request)
#        print('METHOD:',request.method)
        apagar = Contato.objects.filter(id=id)
        if apagar:
            nome = apagar[0].nome
            apagar.delete()
            if not Contato.objects.filter(id=id):
                response = HttpResponse(f'{nome} Removido com SUCESSO')
                response.status_code = 200
                return response
            
@csrf_exempt
def foto(request,foto=None):
    if request.method == 'GET':
    
        try:
            print('FOTO:',foto)
            foto = Contato.objects.filter(foto=f'agenda/fotos/{foto}')[0]
            return FileResponse(foto.foto)
        except ObjectDoesNotExist:
                raise Http404("Foto não encontrada")
        except Exception as exception:
                raise exception
        
    elif request.method == 'POST':
    
        try:
            print('foto-POST:',request.POST)
            foto = Contato.objects.get(pk=request.POST['id'])
            print('foto-FILES:',request.FILES)
            foto.foto = request.FILES['foto']
            foto.save()
            return FileResponse(foto.foto.url)
        except ObjectDoesNotExist:
                raise Http404("Foto não encontrada")
        except Exception as exception:
                raise exception