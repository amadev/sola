# -*- coding: utf-8 -*-
import datetime
from django.db import models


class Contragent(models.Model):
    created = models.DateTimeField(u'добавлено', auto_now_add=True)
    name = models.TextField(u'наименование')
    phone = models.CharField(u'телефон', max_length=255)
    email = models.CharField(u'email', max_length=255)
    address = models.TextField(u'адрес')
    comment = models.TextField(u'описание')

    class Meta:
        abstract = True


class Client(Contragent):
    class Meta:
        verbose_name = u'клиент'
        verbose_name_plural = u'клиенты'

    def __unicode__(self):
        return self.name


class Notary(Contragent):
    class Meta:
        verbose_name = u'нотариус'
        verbose_name_plural = u'нотариусы'

    def __unicode__(self):
        return self.name


class Translator(Contragent):
    class Meta:
        verbose_name = u'переводчик'
        verbose_name_plural = u'переводчики'

    def __unicode__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(u'наименование', max_length=255)

    class Meta:
        verbose_name = u'язык'
        verbose_name_plural = u'языки'

    def __unicode__(self):
        return self.name


class DocumentType(models.Model):
    name = models.CharField(u'наименование', max_length=255)

    class Meta:
        verbose_name = u'тип документа'
        verbose_name_plural = u'типы документов'

    def __unicode__(self):
        return self.name


class Document(models.Model):
    created = models.DateTimeField(u'добавлено', auto_now_add=True)
    date = models.DateField(u'день', default=datetime.date.today())
    client = models.ForeignKey(Client, verbose_name=u'клиент')
    traslator = models.ForeignKey(
        Translator, verbose_name=u'переводчик', null=True, blank=True)
    notary = models.ForeignKey(
        Notary, verbose_name=u'нотариус', null=True, blank=True)
    cost = models.FloatField(u'стоимость')
    expenses_translator = models.FloatField(
        u'расходы переводчик', null=True, blank=True, default=0.0)
    expenses_notary = models.FloatField(
        u'расходы нотариус', null=True, blank=True, default=0.0)
    expenses_other = models.FloatField(
        u'расходы прочее', null=True, blank=True, default=0.0)
    deadline = models.DateTimeField(
        u'срок исполнения', null=True, blank=True)
    status = models.CharField(
        u'статус', max_length=255, choices=((u'accepted', u'принято'),
                                            (u'payed', u'оплачено')))
    payment_type = models.CharField(
        u'расчет', max_length=255, choices=((u'cash', u'наличный'),
                                            (u'', u'безналичный')))
    language = models.ForeignKey(
        Language, verbose_name=u'язык', null=True, blank=True)
    document_type = models.ForeignKey(
        DocumentType, verbose_name=u'тип', null=True, blank=True)
    comment = models.TextField(u'описание', null=True, blank=True)

    class Meta:
        verbose_name = u'документ'
        verbose_name_plural = u'документы'


    def __unicode__(self):
        return u'документ № {} от {}'.format(self.id, self.date)
