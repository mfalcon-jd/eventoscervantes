from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, get_list_or_404, render_to_response
from secciones.models import TipoSeccion

def tipo_seccion(request, slug):
    tipo_seccion = get_object_or_404(TipoSeccion, slug=str(slug))
    ctx = RequestContext(request, {
            'tipo_seccion': tipo_seccion,
        }
    )
    return render_to_response('secciones/tipo_seccion.html', context_instance=ctx)