import requests
from django.conf import settings
from kidconnect.models import Evento
from django.http import JsonResponse
from django.shortcuts import render, redirect

def home(request):
    return render (request,"index.html")

def correo(request):
    return render (request,"correo.html")


def menu(request):
    # Lógica adicional para la página de menú
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
        #      return render (request,'menu.html')#, {'datos':datos}) #'animales' : amimales})
        #else:
            # Manejar errores de solicitud
            #print('Error en la solicitud:', response.status_code)
    #except requests.exceptions.RequestException as e:
        # Manejar errores de conexión
        #print('Error de conexión:', e)

    #return None
    

def alumno(request):  
    url = "https://tmp.enred.cl/kc/rest/get_ficha_all.php"  # URL de la API externa
#    url2 = "http://tmp.enred.cl/rest/get_mensaje.php"
    
    try:
        response = requests.get(url)
#        response2 = requests.get(url2)
        if response.status_code == 200:
            datos = response.json()
#            amimales = response2.json()
#            Procesar los datos obtenidos de la API
            return render (request,'alumno.html', {'datos':datos})#, 'animales' : amimales})
        else:
#            Manejar errores de solicitud
            print('Error en la solicitud:', response.status_code)
    except requests.exceptions.RequestException as e:
#        Manejar errores de conexión
        print('Error de conexión:', e)

    

def docente(request):
    return render(request, "docente.html")

def evento(request):
    return render(request, "evento.html")


# def obtener_usuario_por_rut(request):
#     if 'numrun' in request.GET:
#         numrun = request.GET['numrun']
#         # Realiza la lógica para obtener el usuario por el rut
#         # ...
#         # Supongamos que obtienes el usuario en la variable 'usuario'
#         return JsonResponse({'usuario': usuario})
#     else:
#         return JsonResponse({'error': 'Parámetro numrun faltante en la URL.'})

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





def post_region(request):
    url = 'http://tmp.enred.cl/rest/post_region.php'
    data = {
        # Aquí puedes agregar los datos que deseas enviar en la solicitud POST
        'cod_reg': '1',
        'nom_reg': 'Tarapaca'
    }
    response = requests.post(url, data=data)
    return JsonResponse(response.json())

from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        # Obtén los datos del formulario de inicio de sesión
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        # Construye el cuerpo de la solicitud POST
        data = {
            'rut': usuario,
            'password': contrasena
        }

        # Realiza la solicitud a la API
        api_url = 'http://tmp.enred.cl/kc/rest/login.php'  # Reemplaza con la URL de tu API
        response = requests.post(api_url, json=data)

        # Analiza la respuesta de la API
        if response.status_code == 200:
            # Los datos son válidos
            return redirect('menu')
        else:
            # Los datos son inválidos o hubo un error en la solicitud a la API
            error_message = 'Error en la solicitud a la API'
            if response.status_code == 401:
                error_message = 'Datos inválidos'
            return render(request, 'index.html', {'error_message': error_message})

    return render(request, 'index.html')

