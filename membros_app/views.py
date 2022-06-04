from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Membro
from .forms import MembroForm

# Create your views here.
@login_required(login_url='account_login')
def listar_membros(request):
    membros = Membro.objects.all()
    
    return render(request, 'membro_list.html', {'membros': membros})


#Criar view do formulário
@login_required(login_url='account_login')
def form_membros(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form  = MembroForm()
        else:
            membro = Membro.objects.get(pk = id)
            form  = MembroForm(instance = membro)
        return render(request, 'membro_form.html', { 'form':form })
    else:
        if id == 0:
            form  = MembroForm(request.POST)
        else:
            membro = Membro.objects.get(pk = id)
            form  = MembroForm(request.POST, instance = membro)
            
        if form.is_valid():
            form.save()
        return redirect('listar_membros')  
    
@login_required(login_url='account_login')
def excluir_membro(request, id):
    membro = Membro.objects.get(pk = id)
    membro.delete()
    return redirect('listar_membros')

@login_required(login_url='account_login')
def visualizar_membro(request, id):
    membro = Membro.objects.get(pk = id)
    return render(request, 'membro_view.html', {'membro': membro})