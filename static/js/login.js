function guardarValor() {
  var usuario = document.getElementById('myInput').value;
  var contrasena = document.getElementById('mypass').value;

  var data = {
    rut: usuario,
    password: contrasena
  };

  var api_url = 'http://tmp.enred.cl/kc/rest/login.php';

  fetch(api_url, {
    method: 'POST',
    body: JSON.stringify(data)
  })
  .then(function(response) {
    if (response.status === 200) {
      // Los datos son válidos
      window.location.href = 'menu.html';
    } else {
      // Los datos son inválidos o hubo un error en la solicitud a la API
      var error_message = 'Error en la solicitud a la API';
      if (response.status === 401) {
        error_message = 'Datos inválidos';
      }
      document.getElementById('error-message').innerText = error_message;
    }
  })
  .catch(function(error) {
    console.error('Error en la solicitud:', error);
  });
    var valor = document.getElementById("myInput").value;
    obtenerPersonaPorRut(valor);
  }


  function obtenerPersonaPorRut(rut) {
    var api_url = 'http://tmp.enred.cl/kc/rest/get_usuarios.php?rut=' + rut;
  
    fetch(api_url)
      .then(function(response) {
        if (response.status === 200) {
          return response.json();
        } else {
          throw new Error('Error en la solicitud a la API');
        }
      })
      .then(function(responseData) {
        if (responseData.success) {
          var persona = responseData.data;
          console.log(persona);
  
          // Guardar el resultado en el local storage
          localStorage.setItem('persona', JSON.stringify(persona));
          console.log('Resultado guardado en el local storage');
        } else {
          console.log('No se encontró ninguna persona con el rut dado');
        }
      })
      .catch(function(error) {
        console.error('Error en la solicitud:', error);
      });
  }