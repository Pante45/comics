import uuid

from django.db import models


class Editorial(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Comic(models.Model):
    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        related_name='comics',
    )
    titulo = models.CharField(max_length=200)
    imagen_portada = models.ImageField(upload_to='portadas/')
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    numero_tomo = models.PositiveIntegerField()
    tapa_dura = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Cómic'
        verbose_name_plural = 'Cómics'
        ordering = ['titulo', 'numero_tomo']

    def __str__(self):
        return f'{self.titulo} (Tomo {self.numero_tomo})'


class Reserva(models.Model):
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name='reservas',
    )
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    rut = models.CharField(max_length=12)
    cantidad = models.PositiveSmallIntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    codigo = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-fecha_reserva']

    def __str__(self):
        return f'{self.codigo} - {self.comic.titulo}'