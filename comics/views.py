
from django.shortcuts import render, get_object_or_404
from django.db import transaction

from .models import Comic, Editorial
from .forms import ReservaForm


def catalogo(request):
    comics = Comic.objects.filter(disponible=True)

    busqueda = request.GET.get('buscar', '').strip()
    editorial_id = request.GET.get('editorial', '')

    if busqueda:
        comics = comics.filter(titulo__icontains=busqueda)

    if editorial_id:
        comics = comics.filter(editorial_id=editorial_id)

    editoriales = Editorial.objects.all()

    return render(request, 'comics/catalogo.html', {
        'comics': comics,
        'editoriales': editoriales,
        'busqueda': busqueda,
        'editorial_seleccionada': editorial_id,
    })


def detalle_comic(request, comic_id):
    comic = get_object_or_404(
        Comic,
        id=comic_id,
        disponible=True
    )

    return render(request, 'comics/detalle.html', {
        'comic': comic
    })


def reservar_comic(request, comic_id):
    comic = get_object_or_404(
        Comic,
        id=comic_id,
        disponible=True
    )

    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
    else:
        formulario = ReservaForm()

    return render(request, 'comics/reservar.html', {
        'comic': comic,
        'formulario': formulario,
    })
