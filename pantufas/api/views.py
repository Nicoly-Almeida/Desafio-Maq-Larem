from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pprint import pprint
from api.models import Usuario, Contato
from django.contrib.auth.decorators import login_required

from api.forms import ContatoForm


def loginView(request):
    if request.user.is_authenticated:
        return redirect("/contatos")
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        data = request.POST
        user = authenticate(request, username=data["username"], password=data["password"])
        if user:
            login(request, user)
            return redirect("/contatos")

    return redirect("/")


def registerView(request):
    if request.user.is_authenticated:
        return redirect("/contatos")
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        data = request.POST

        if (data["password"] == data["re_password"]):
            user = Usuario()
            user.username=data["username"]
            user.celular=data["celular"]
            user.set_password(raw_password = data["password"])

            user.save()
            return redirect("/")
    
    return HttpResponse("")


@login_required(login_url = "/")
def contatoView(request):
    if request.method == "GET":
        listar_contatos = request.user.contatos.all()
        lista = []
        for contato in listar_contatos:
            lista.append(contato)
        pprint(listar_contatos)
        return render(request, "contatos.html", context = {"listar": lista})

    elif request.method == "POST":
        data = request.POST

        contato = Contato()
        contato.nome=data["nome"]
        contato.celular=data["celular"]
        contato.email=data["email"]
        contato.endereco=data["endereco"]
        contato.dia=data["dia"]
        contato.mes=data["mes"]
        contato.ano=data["ano"]
        
        contato.save()
        user = request.user
        user.contatos.add(contato)
        user.save()
        return redirect("/contatos")


@login_required(login_url = "/")
def logoutView(request):
    logout(request)
    return redirect("/")


@login_required(login_url = "/")
def deleteView(request, id):
    contato = Contato.objects.get(id = id)
    user = request.user
    user.contatos.remove(contato)
    user.save()
    contato.delete()
    return redirect("/contatos")


@login_required(login_url= '/')
def editView(request, id):

    contato = Contato.objects.get(id = id)

    form = ContatoForm(instance=contato)

    if request.method == 'POST':

        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect("/contatos")

    context = {
        'contato': contato,
        'form': form
    }
    return render(request, "contato_edit.html", context)
