from django.shortcuts import render

# Create your views here.
def inicio(request):
    temas = [
        {
            'nombre': 'Ciberseguridad',
            'descripcion': 'Conoce conceptos relacionados a la ciberseguridad.'
        },
        {
            'nombre': 'Videojuegos',
            'descripcion': 'Conoce el mundo de los videojuegos .'
        }
    ]

    contexto = {
        'temas': temas
    }

    return render(request, 'inicio_ortiz/inicio.html', contexto)



def ciberseguridad(request):
    return render(request, 'inicio_ortiz/ciberseguridad.html')


def videojuegos(request):
    return render(request, 'inicio_ortiz/videojuegos.html')