from django.db import models
from django.shortcuts import resolve_url as r

PHONE_TYPE = (
    ('pri', 'principal'),
    ('com', 'comercial'),
    ('res', 'residencial'),
    ('cel', 'celular'),
    ('cl', 'Claro'),
    ('oi', 'Oi'),
    ('t', 'Tim'),
    ('v', 'Vivo'),
    ('n', 'Nextel'),
    ('fax', 'fax'),
    ('o', 'outros'),
)


class TimeStampedModel(models.Model):
    created = models.DateTimeField('creado en', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField('modificado en', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Asistencia(models.Model):
    pase = models.BooleanField('pase', default=True)
    consulta = models.BooleanField('consulta', default=False)
    aporte = models.PositiveIntegerField()


class Address(models.Model):
    address = models.CharField('dirección', max_length=100, blank=True)
    complement = models.CharField('complemento', max_length=100, blank=True)
    district = models.CharField('barrio', max_length=100, blank=True)
    city = models.CharField('ciudad', max_length=100, blank=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel, Address, Asistencia):
    first_name = models.CharField('nombre', max_length=50)
    last_name = models.CharField('apellido', max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    birth_date = models.DateField()
    blocked = models.BooleanField('bloqueado', default=False)

    class Meta:
        ordering = ['first_name']
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return ' '.join(filter(None, [self.first_name, self.last_name]))

    full_name = property(__str__)

    def get_absolute_url(self):
        return r('core:person_detail', pk=self.pk)


class Phone(models.Model):
    phone = models.CharField('telefono', max_length=20, blank=True)
    person = models.ForeignKey('Person', on_delete=models.PROTECT)
    phone_type = models.CharField('tipo', max_length=3, choices=PHONE_TYPE, default='pri')

    def __str__(self):
        return self.phone
