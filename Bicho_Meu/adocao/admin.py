from django.contrib import admin

from .models import Cliente, Doador, Animal, Adocao, Raca


class AnimaisInline(admin.TabularInline):
    model = Animal
    extra = 3

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'genero', 'registro_eh_antigo')

    list_filter = ['registro']

    search_fields = ['nome']

    fieldsets = [(None, {
        'fields': ['nome', 'genero', 'endereco', 'telefone', 'email']}),
        ('Documentos', {
            'fields': ['cpf'],
            'classes': ['collapse']}),
        ]
class DoadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'genero', 'registro_eh_antigo')

    list_filter = ['registro']

    search_fields = ['nome']

    fieldsets = [(None, {
        'fields': ['nome', 'genero', 'endereco', 'telefone', 'email']}),
        ('Documentos', {
            'fields': ['cpf'],
            'classes': ['collapse']}),
        ]

class RacaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'porte')

    inlines = [AnimaisInline]

    list_filter = ['porte']

    search_fields = ['nome']


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca')

    list_filter = ['raca']

    search_fields = ['nome']


class AdocaoAdmin(admin.ModelAdmin):
    list_filter = ['registro']

    search_fields = ['animal__nome', 'cliente__nome']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Doador, DoadorAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Adocao, AdocaoAdmin)
admin.site.register(Raca, RacaAdmin)
