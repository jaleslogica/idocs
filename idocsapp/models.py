from django.db import models
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField


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

    UF_CHOICES = (
        (u'ce', u'CE'),
        (u'pb', u'PB'),
        (u'sp', u'SP'),
        (u'rj', u'RJ'),
    )

    contato_nome = models.CharField(max_length=50, verbose_name='Nome')
    contato_tel = models.IntegerField(verbose_name='Telefone')
    contato_email = models.EmailField(max_length=100, verbose_name='E-mail')
    contato_nascimento = models.DateField(verbose_name='Dta de Nascimento')
    contato_sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
    contato_estadocivil = models.CharField(max_length=50, choices=ESTADO_CIVIL_CHOICES, verbose_name='Estado Civil')
    contato_favorito = models.BooleanField(verbose_name='Favorito')
    contato_endereco = models.CharField(max_length=255, verbose_name=u'Endereco',
                                        help_text='Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Rua Martinho Estrela,  1229')
    contato_bairro = models.CharField(max_length=255, verbose_name='Bairro')
    contato_cidade = models.CharField(max_length=255, verbose_name='Cidade',
                                      help_text="Para uma melhor localizacao no mapa, preencha sem abreviacoes. Ex: Belo Horizonte")
    contato_estado = models.CharField(max_length=2, null=True, blank=True, choices=UF_CHOICES, verbose_name='Estado')
    contato_position = GeopositionField(verbose_name=u'Geolocalizacao',
                                        help_text="Nao altere os valores calculados automaticamente de latitude e longitude")


class Meta:
    verbose_name, verbose_name_plural = u"Contato", u"Contatos"
    ordering = ('contato_endereco',)


def __unicode__(self):
    return u"%s" % self.contato_endereco, self.contato_email


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
