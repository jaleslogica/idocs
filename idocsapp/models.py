from django.db import models
import datetime
from django.utils import timezone

class Contatos(models.Model):


    SEXO_CHOICES = (

        (u'masculino', u'Masculino'),
        (u'feminino', u'Feminino'),
    )

    ESTADO_CIVIL_CHOICES = (

        (u'solteiro', u'Solteiro'),
        (u'divorciado', u'Divorciado'),
        (u'casado', u'Casado'),
        (u'viuvo', u'Viuvo'),

    )

    contato_nome = models.CharField(max_length=50)
    contato_tel = models.IntegerField(verbose_name='Telefone')
    contato_email = models.EmailField(max_length=100, verbose_name='E-mail')
    contato_nascimento = models.DateField()
    contato_sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
    contato_estadocivil = models.CharField(max_length=50, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado Civil')
    contato_favorito = models.BooleanField(verbose_name='Favorito')

    def __unicode__(self):
        return self.contato_email


class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField()

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text