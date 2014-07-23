# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from secciones.models import TipoSeccion, Seccion

def index(request):
    return render(request,'index.html')

def pagina(request, slug):
    pagina = get_object_or_404(TipoSeccion, slug=str(slug))
    secciones = pagina.seccion_set.all().order_by('id')
    ctx = RequestContext(request, {
            'pagina': pagina,
            'secciones': secciones,
        }
    )
    return render_to_response('secciones/pagina.html', context_instance=ctx)

def seccion(request, slug):
    seccion = get_object_or_404(Seccion, slug=str(slug))
    ctx = RequestContext(request, {
            'seccion': seccion,
        }
    )
    return render_to_response('secciones/seccion.html', context_instance=ctx)

def contacto(request):
    return render(request,'contacto.html')