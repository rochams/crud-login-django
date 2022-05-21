from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def cadastro(request):
    
    if request.method=='GET':
        return render(request, 'cadastro.html')

    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=usuario).first()

        if user:
            return HttpResponse('Já existe um usuário com o e-mail cadastrado.')

        user = User.objects.create_user(
            username=usuario,
            email=email,
            password=senha
        )
        
        user.save()

        users = User.objects.all()
        context = {
                    'users': users
                }

        return render(request, 'index.html', context)



@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        grant = authenticate(username=usuario, password=senha)

        if grant:
            users = User.objects.all()
            context = {
                'users': users
            }
            usuario = User.objects.filter(username=usuario).first()
            return render(request, 'index.html', context)


