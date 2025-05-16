from django.db import models

# Create your models here.

class Responsavel (models.Model):
    nome = models.CharField(max_length=100, null = False, blank = False)
    num_cpf = models.CharField(max_length=11, null = False, blank = False)


class Todo (models.Model):
    title = models.CharField(max_length=100, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add= True, null= False, blank = False)
    deadline = models.DateTimeField(null = False, blank = False)
    pessoa_responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
