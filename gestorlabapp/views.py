from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login")
def PaginaInicial(request):
    return render(request,'PageInicial.html')