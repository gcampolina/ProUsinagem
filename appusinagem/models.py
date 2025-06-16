from django.db import models



class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Service(models.Model):
    contratante = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nome_servico = models.CharField(max_length=100)
    detalhes = models.TextField()
    data_servico = models.DateField()
    data_entrega = models.DateField()
    contato = models.CharField(max_length=15)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Ativo" ,choices=[('Ativo', 'Ativo'), ('Finalizado', 'Finalizado')])
    imagem = models.ImageField(upload_to='servicos/', blank=True, null=True)

    def __str__(self):
        return f"{self.contratante} - {self.nome_servico}"


