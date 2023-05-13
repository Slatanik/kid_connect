import requests
from django.conf import settings
from kidconnect.models import Evento
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect

def home(request):
    return render (request,"index.html")

def correo(request):
    return render (request,"correo.html")

def menu(request):
            if request.method == 'POST':
                usuario = request.POST.get('usuario', '')  # Obtén el valor ingresado en el campo "usuario"
                return render(request, 'menu.html', {'usuario': usuario})
            else:
                return render(request, 'menu.html')
    #url = "http://tmp.enred.cl/rest/get_region.php"  # URL de la API externa
    #url2 = "http://tmp.enred.cl/rest/get_mensaje.php"
    #headers = {
        #'Authorization': 'Bearer ' + settings.API_TOKEN  # Ejemplo de encabezado de autenticación
    #}
    #try:
        # response = requests.get(url)
        # response2 = requests.get(url2)
        # if response.status_code == 200:
        #     datos = response.json()
        #     amimales = response2.json()
        #     Procesar los datos obtenidos de la API
              return render (request,'menu.html')#, {'datos':datos}) #'animales' : amimales})
        #else:
            # Manejar errores de solicitud
            #print('Error en la solicitud:', response.status_code)
    #except requests.exceptions.RequestException as e:
        # Manejar errores de conexión
        #print('Error de conexión:', e)

    #return None
    

def alumno(request):
    url = "http://tmp.enred.cl/rest/get_ficha_all.php"  # URL de la API externa
    #url2 = "http://tmp.enred.cl/rest/get_mensaje.php"
    #headers = {
        #'Authorization': 'Bearer ' + settings.API_TOKEN  # Ejemplo de encabezado de autenticación
    #}
    try:
        response = requests.get(url)
        #response2 = requests.get(url2)
        if response.status_code == 200:
            datos = response.json()
            #amimales = response2.json()
            # Procesar los datos obtenidos de la API
            return render (request,'alumno.html', {'datos':datos})#, 'animales' : amimales})
        else:
            # Manejar errores de solicitud
            print('Error en la solicitud:', response.status_code)
    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión
        print('Error de conexión:', e)

    return render (request, 'alumno.html')

def docente(request):
    return render(request, "docente.html")

def evento(request):
    return render(request, "evento.html")


def obtener_usuario_por_rut(request):
    if 'numrun' in request.GET:
        numrun = request.GET['numrun']
        # Realiza la lógica para obtener el usuario por el rut
        # ...
        # Supongamos que obtienes el usuario en la variable 'usuario'
        return JsonResponse({'usuario': usuario})
    else:
        return JsonResponse({'error': 'Parámetro numrun faltante en la URL.'})

def llamar_endpoint(request):
    if request.method == 'POST':
        json_data = request.POST.get('json_data')  # Obtén el JSON enviado desde el frontend
        url = "http://example.com/api/endpoint"  # URL del endpoint externo

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, headers=headers, json=json_data)
            if response.status_code == 200:
                datos = response.json()
                return JsonResponse(datos)
            else:
                return JsonResponse({'error': 'Error en la solicitud: {}'.format(response.status_code)})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': 'Error de conexión: {}'.format(e)})

    return JsonResponse({'error': 'Método no permitido.'})


