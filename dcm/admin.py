# -*- coding: utf-8 -*-
from dcm import models as dmodels
from django.contrib import admin


class DocumentAdmin(admin.ModelAdmin):
    pass


class DocumentTypeAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


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
