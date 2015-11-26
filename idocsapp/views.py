import json
import mimetypes
from django.core.serializers import json
from django.shortcuts import render

from idocsapp.models import Question
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def proposta(request):
    return render(request, "proposta.html")


def empresa(request):
    return render(request, "empresa.html")


def download(request):
    return render(request, "download.html")


def produtos(request):
    return render(request, "produtos.html")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def enviar_proposta(request):
    formulario = FormProposta(request.POST)
    if formulario.is_valid():
        try:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            assunto = request.POST.get('assunto')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')
            texto_mensagem = request.POST.get('mensagem')
            mensgem = """
                    Remetente: %s
                    E-ail: %s
                    Cidade: %s
                    Estado: %s
                    Telefone: %s
                    Assunto: %s
                    Mensagem:
                    %s
                    """ % (nome, email, cidade, estado, telefone, assunto, texto_mensagem)
            send_mail('Contato do site', mensagem, )
            resposta = [{'resposta': 'Email enviado com sucesso'}]
            json.simplejson.dumps(resposta)
            return HttpResponse(json, mimetypes="application/json")

        finally:
            texto_mensagem  # isso foi eu que completei pra ter uma ideia, verificar nuvols favoritos

