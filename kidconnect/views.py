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
        api_url = 'http://tmp.enred.cl/kc/rest/login.php'  
        response = requests.post(api_url, json=data)
        data = response.json()
        api_urlget_userdata = 'http://tmp.enred.cl/kc/rest/get_user_id.php?nombreFuncion={}&rut_us={}'.format( "buscarUsuarioPorRut", usuario)

        if data['valid']:
            request.session['user_id'] = usuario
        
            dataUsuario = requests.get(api_urlget_userdata)
            print(dataUsuario)
            dataUsuario = dataUsuario.json()

            request.session['perfil'] = dataUsuario["data"]["tipo_us_cod_tip"]#aqui estoy asignando la respuesta de cod_tip que devolvera api si metemeto Cod_tip en .php de la api
            request.session['nombreDeUsuario'] = dataUsuario["data"]["nom_us"]
            return redirect('menu')

        else:
            print("no valido")
            return render(request, 'index.html', {'mensaje':'Usuario Incorrecto'})
        # Analiza la respuesta de la API
     #   if response.status_code == 200:
     #       # Los datos son válidos
     #       return redirect('menu')
     #   else:
    #        # Los datos son inválidos o hubo un error en la solicitud a la API
     #       error_message = 'Error en la solicitud a la API'
    #        if response.status_code == 401:
     #           error_message = 'Datos inválidos'
    #        return render(request, 'index.html', {'error_message': error_message})

  #  return render(request, 'index.html')

import requests

def crearAlumno(request):
    if request.method == "GET":
        return render(request, "crearAlumno.html")
    else:
        rut_alu = request.POST.get('rut_alu', None)
        dv_alu = request.POST.get('dv_alu', None)
        nom_alu = request.POST.get('nom_alu', None)
        ap_pat_alu = request.POST.get('ap_pat_alu', None)
        ap_mat_alu = request.POST.get('ap_mat_alu', None)
        dir_alu = request.POST.get('dir_alu', None)
        curso_cod_cur = request.POST.get('curso_cod_cur', None)
        curso_cod_niv = request.POST.get('curso_cod_niv', None)
        usuario_rut_us = request.POST.get('usuario_rut_us', None)
        usuario_jardin_cod_jar = request.POST.get('usuario_jardin_cod_jar', None)
        usuario_cod_tip = request.POST.get('usuario_cod_tip', None)
        curso_cod_jor = request.POST.get('curso_cod_jor', None)
        curso_cod_jar = request.POST.get('curso_cod_jar', None)

        data = {
            'rut_alu': rut_alu,
            'dv_alu': dv_alu,
            'nom_alu': nom_alu,
            'ap_pat_alu': ap_pat_alu,
            'ap_mat_alu': ap_mat_alu,
            'dir_alu': dir_alu,
            'curso_cod_cur': curso_cod_cur,
            'curso_cod_niv': curso_cod_niv,
            'usuario_rut_us': usuario_rut_us,
            'usuario_jardin_cod_jar': usuario_jardin_cod_jar,
            'usuario_cod_tip': usuario_cod_tip,
            'curso_cod_jor': curso_cod_jor,
            'curso_cod_jar': curso_cod_jar
        }

        api_url = 'http://tmp.enred.cl/kc/rest/post_alumno.php'
        response = requests.post(api_url, json=data)

        if rut_alu is None or dv_alu is None or nom_alu is None or ap_pat_alu is None or ap_mat_alu is None or dir_alu is None or curso_cod_cur is None or curso_cod_niv is None or usuario_rut_us is None or usuario_jardin_cod_jar is None or usuario_cod_tip is None or curso_cod_jor is None or curso_cod_jar is None:
            return render(request, "crearAlumno.html", {'message':'NO SE HA PODIDO CREAR EL ALUMNO'})
        
        # Aquí puedes realizar las operaciones necesarias con los datos recibidos
        
        return render(request, "crearAlumno.html")
