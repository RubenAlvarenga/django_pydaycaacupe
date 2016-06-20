#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class TimeStampModel(models.Model):
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Categoria(models.Model):
    nombre = models.CharField(max_length=140)
    def __unicode__(self):
        return u'%s' % (self.nombre)



class Noticias(TimeStampModel):
    titulo = models.CharField(max_length=140)
    categorias = models.ManyToManyField(Categoria)
    creado_por = models.ForeignKey(User, on_delete=models.PROTECT)
    noticia = models.TextField()

    def save(self, *args, **kwargs):
        titulo = getattr(self, 'titulo')
        if titulo: setattr(self, 'titulo', titulo.title())
        super(Noticias, self).save(*args, **kwargs)


    @property
    def get_comentarios(self):
        return Comentario.objects.get(noticia = self)

    def __unicode__(self):
        return u'%s' % (self.titulo)




class Comentario(TimeStampModel):
    noticia = models.ForeignKey(Noticias, on_delete=models.PROTECT)
    comentario = models.CharField(max_length=140)
    email = models.EmailField(max_length=50, 
        validators=[
            RegexValidator(
                regex = '^[a-zA-Z]*@uninorte.com|[a-zA-Z]*gmail.com$',
                message = "Solo uninorte y gmail"
                )
            ]
        )    

    def __unicode__(self):
        return u'%s' % (self.comentario)
