from Carbon.Aliases import true
from django import forms
from django.contrib import admin
from idocsapp.models import Artigo, Question, Choice, Car, Contatos


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # Criando Fieldsets para os atributos da classe
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Comando pra colocar uma tabela na mostragem da classe
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Comando pra colocar um filtro
    list_filter = ['pub_date']
    # Comando para colocar um buscar
    search_fields = ['question_text', 'pub_date']
    # Comando pra colocar os booes de salvar no topo
    save_on_top = true


class ContatosForm(forms.ModelForm):
    class Media:
        css = {
            'all': ('static/css/geoposition_override.css',)
        }
        js = ('static/js/geoposition_override.js',)


class ContatosAdmin(admin.ModelAdmin):
    form = ContatosForm
    list_display = ('contato_nome', 'contato_email', 'contato_tel', '' 'contato_cidade', 'contato_estado')
    list_filter = ['contato_sexo']
    search_fields = ['contato_nome', 'contato_email','contato_endereco', 'contato_cidade',]
    # pra deixar os botoes tambem no topo
    save_on_top = true



# Comando para registrar as classe a admin do django
admin.site.register(Question, QuestionAdmin)
admin.site.register(Artigo)
admin.site.register(Choice)
admin.site.register(Car)
admin.site.register(Contatos, ContatosAdmin)
