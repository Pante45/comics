from django.shortcuts import render
from .models import Comic, Editorial


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