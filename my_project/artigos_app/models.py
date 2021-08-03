from django.db import models

# Create your models here.
class Autor(models.Model):
  nome = models.CharField(
    verbose_name="Nome do autor",
    max_length=255
  )
  endereco = models.CharField(
    verbose_name="Endereço do autor",
    max_length=255
  )
  site = models.URLField(
    blank=True,
    null=True
  )
  email = models.EmailField()

  def __str__(self):
    return self.nome + ' - ' + self.email

class Artigo(models.Model):
  autor = models.ForeignKey(
    Autor,
    on_delete=models.CASCADE
  )
  titulo = models.CharField(
    verbose_name="Titulo do artigo",
    max_length=200
  )
  publicado = models.DateField(
    auto_now=True,
  )
  atualizado = models.DateField(
    auto_now_add=True
  )
  texto = models.TextField()

  def __str__(self):
    return self.titulo