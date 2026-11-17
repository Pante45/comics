
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.db.models import F
from django.http import Http404

from .models import Comic, Editorial, Reserva
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

    # No permitir entrar al formulario si está agotado.
    if comic.stock == 0:
        raise Http404('Este cómic está agotado.')

    if request.method == 'POST':
        formulario = ReservaForm(request.POST)

        if formulario.is_valid():
            cantidad = formulario.cleaned_data['cantidad']

            with transaction.atomic():
                actualizados = Comic.objects.filter(
                    pk=comic.pk,
                    disponible=True,
                    stock__gte=cantidad
                ).update(stock=F('stock') - cantidad)

                if actualizados:
                    reserva = formulario.save(commit=False)
                    reserva.comic = comic
                    reserva.save()

                    # Redirigir para evitar repetir el POST.
                    return redirect(
                        'comprobante_reserva',
                        codigo=reserva.codigo
                    )

            # Si otro cliente reservó antes, actualizar stock.
            comic.refresh_from_db()

            formulario.add_error(
                'cantidad',
                f'Solo quedan {comic.stock} ejemplares disponibles.'
            )

    else:
        formulario = ReservaForm()

    return render(request, 'comics/reservar.html', {
        'comic': comic,
        'formulario': formulario,
    })


def comprobante_reserva(request, codigo):
    reserva = get_object_or_404(
        Reserva.objects.select_related('comic'),
        codigo=codigo
    )

    total = reserva.comic.precio * reserva.cantidad

    return render(request, 'comics/reserva_exitosa.html', {
        'reserva': reserva,
        'comic': reserva.comic,
        'total': total,
    })
