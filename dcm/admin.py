# -*- coding: utf-8 -*-
from dcm import models as dmodels
from django.contrib import admin


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'date', 'client', 'cost']
    radio_fields = {'status': admin.HORIZONTAL,
                    'payment_type': admin.HORIZONTAL}

    list_filter = (
        'date',
        'status',
        'payment_type',
        'language',
        'document_type',
        'traslator',
        'notary'
    )

    search_fields = ('comment', 'client__name')
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return instance


class DocumentTypeAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    radio_fields = {'ctype': admin.HORIZONTAL}
    fields = ['ctype', 'name', 'phone', 'email', 'address', 'comment']


class TranslatorAdmin(admin.ModelAdmin):
    pass


class NotaryAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(dmodels.Document, DocumentAdmin)
admin.site.register(dmodels.DocumentType, DocumentTypeAdmin)
admin.site.register(dmodels.Client, ClientAdmin)
admin.site.register(dmodels.Translator, TranslatorAdmin)
admin.site.register(dmodels.Notary, NotaryAdmin)
admin.site.register(dmodels.Language, LanguageAdmin)
