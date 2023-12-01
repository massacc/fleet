from django.db import models
from django.utils.translation import gettext_lazy as _

class Invoice(models.Model):
    PAYMENT_METHODS = [
        (0, _('Cash')),
        (1, _('Transfer'))
    ]
    created = models.DateField(auto_now_add=True, verbose_name=_('Date of creation'))
    updated = models.DateField(auto_now=True, verbose_name=_('Last modified'))
    delivered = models.DateField(verbose_name=_('Delivery date'))
    issued = models.DateField(verbose_name=_('Date of issue'))
    payment_date = models.DateField(verbose_name=_('The payment date'))
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHODS, verbose_name=_('Payment method'))
    #customer = models.ForeignKey(Customer, related_name='invoices', on_delete=models.PROTECT, verbose_name=_('Customer'))
    #company = models.ForeignKey(Company, related_name='invoices', on_delete=models.PROTECT, verbose_name=_('Company'))
    order = models.IntegerField(default=0)
    number = models.CharField(max_length=100)
    #currency = models.ForeignKey(Currency, )
#typDok,dataDok,dataOper,dataWpl,dataWpr,termPlatn,numerDok,trescDok,waluta,dataWal,kursWal,tabKurs,idKth,kolejnosc,jpk_v7

class InvoiceItem(models.Model):
    description = models.CharField(max_length=200, verbose_name=_('Goods or service'))
    #measure  = models.ForeignKey(Measure, related_name='invoice_items', verbose_name=_('Unit of measurement'))
    number = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Number of items'))
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Unit price without tax'))
    #currency_table = models.ForeignKey(Currency, related_name='invoice_items', on_delete=models.PROTECT)
    #tax_rate=models.ForeignKey(TaxRate, related_name='invoice_items')
    net = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Net amount'))
    tax = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Tax amount'))
    gross = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_('Gross amount'))

    
class AccountingDocument(models.Model):
    pass

class Company(models.Model):
    pass

class Customer(models.Model):
    pass

#CREATE TABLE stawki_vat_def (nazwa TEXT, stawka REAL, data_od TEXT, data_do TEXT,aktywna INTEGER)