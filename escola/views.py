from django.shortcuts import render
from escola.forms import ProfessorForm
#from django.http import HttpResponse, request

def ProfessorViews(request):
    form = ProfessorForm(request.POST)
    obj = {
        'title':'Professor',
        'content':'Estou iniciando a página professor',
        'formulario': form,
    
    }
    
    return render(request, 'professor.html', obj)
