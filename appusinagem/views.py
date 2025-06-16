from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceForm, ClientForm 
from .models import Service, Clientes
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_GET

def home(request):
    return render(request,'home.html')


def listaservicos(request):
    finalizados = Service.objects.filter(status="Finalizado")
    return render(request, 'lista-servicos.html', {'finalizados': finalizados})


def servicos(request):
    query = request.GET.get('q')
    if query:
        servicos_ativos = Service.objects.filter(
            status="Ativo",
            contratante__nome__icontains=query
        ).order_by('nome_servico')
    else:
        servicos_ativos = Service.objects.filter(status="Ativo").order_by('nome_servico')
    return render(request, 'servicos.html', {'servicos_ativos': servicos_ativos})





def novoservico(request):
    return render(request, 'novo-servico.html')


def agenda(request):
    return render(request, 'agenda.html')



def clientes(request):
    query = request.GET.get('q')
    if query:
        clientes = Clientes.objects.filter(nome__icontains=query).order_by('nome')
    else:
        clientes = Clientes.objects.all().order_by('nome')
    return render(request, 'clientes.html', {'clientes': clientes})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('clientes')
    else:
        form = ClientForm()
    return render(request, 'novo-cliente.html', {'form': form})


def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('clientes')
    else:
        form = ClientForm(instance=cliente)

    return render(request, 'novo-cliente.html', {'form': form})

def excluir_cliente(request, cliente_id):
    cliente = get_object_or_404(Clientes, id=cliente_id)

    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return redirect('clientes')

    return render(request, 'confirmar_exclusao_cliente.html', {'cliente': cliente})



def novoservico(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            # Lógica de salvamento manual
            contratante = form.cleaned_data['contratante']
            nome_servico = form.cleaned_data['nome_servico']
            detalhes = form.cleaned_data['detalhes']
            data_servico = form.cleaned_data['data_servico']
            data_entrega = form.cleaned_data['data_entrega']
            contato = form.cleaned_data['contato']
            total = form.cleaned_data['total']

            

            # Crie o objeto Pedido
            servico = Service.objects.create(
                contratante=contratante,
                nome_servico=nome_servico,
                detalhes=detalhes,
                data_servico=data_servico,
                data_entrega=data_entrega,
                contato=contato,
                total=total,
            )
                
            messages.success(request, 'Serviço adicionado com sucesso!')
            return redirect('servicos')


    else:
        form = ServiceForm()

    return render(request, 'novo-servico.html', {'form': form})





def finalizar_servico(request, service_id):
    # Recupera o serviço que será finalizado
    service = get_object_or_404(Service, id=service_id)

    # Marca o serviço como finalizado
    service.status = "Finalizado"
    service.save()

    # Redireciona para a página de serviços (ou outra página que liste os serviços)
    return redirect('servicos')

def reativar_servico(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.status = "Ativo"  # Marca o serviço como não finalizado
    service.save()
    return redirect('lista-servicos')  # Redireciona para a página de serviços finalizados

def excluir_servico(request, service_id):
    if request.method == 'POST':
        service = get_object_or_404(Service, id=service_id)
        service.delete()
    return redirect('servicos')


def editar_servico(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        # Preenche o formulário com os dados do POST
        form = ServiceForm(request.POST)
        if form.is_valid():
            # Salva as alterações manualmente no banco de dados
            service.contratante = form.cleaned_data['contratante']
            service.nome_servico = form.cleaned_data['nome_servico']
            service.detalhes = form.cleaned_data['detalhes']
            service.data_servico = form.cleaned_data['data_servico']
            service.data_entrega = form.cleaned_data['data_entrega']
            service.contato = form.cleaned_data['contato']
            service.total = form.cleaned_data['total']
            service.save()
            return redirect('servicos')  # Redireciona para a página de serviços
    else:
        # Preenche o formulário com os dados existentes do serviço
        initial_data = {
            'contratante': service.contratante,
            'nome_servico': service.nome_servico,
            'detalhes': service.detalhes,
            'data_servico': service.data_servico.strftime('%Y-%m-%d'),
            'data_entrega': service.data_entrega.strftime('%Y-%m-%d'),
            'contato': service.contato,
            'total': service.total,
        }
        form = ServiceForm(initial=initial_data)

    return render(request, 'novo-servico.html', {'form': form})