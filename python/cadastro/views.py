from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/lista_pessoas.html', {'pessoas': pessoas})

def adiciona_pessoa(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/form_pessoa.html', {'form': form})
