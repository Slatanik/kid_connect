const form = document.getElementById('Buscar');
form.addEventListener('click', function(event) {
  event.preventDefault(); // Evita la recarga de la página
  const rut = document.getElementById('rutBusqueda');
        fetch(`http://tmp.enred.cl/kc/rest/get_ficha_id.php?nombreFuncion=buscarFichaPorRut&rut_alumno=${rut.value}`, {
          method: 'GET',
        })
          .then(response => {
            if (!response.ok) {
              throw new Error('Error al enviar la solicitud');
            }
            return response.json();
          })
          .then(data => {
            const nombreAlumno = document.getElementById('rut_alumno');
            const fecha = document.getElementById('fecha');
            const contenido = document.getElementById('contenido');
            nombreAlumno.textContent = data.data.alumno_rut_alu
            fecha.textContent = data.data.fec_cre
            contenido.textContent = data.data.con_fc
          })
          .catch(error => {
            console.error(error);
          });
      });


    //   const form = document.getElementById('miFormulario');
    //   form.addEventListener('submit', function(event) {
    //     event.preventDefault(); // Evita que la página se recargue al enviar el formulario
        
    //     const datos = new FormData(form); // Obtiene los datos del formulario

    //     fetch('http://tmp.enred.cl/kc/rest/post_ficha.php', {
    //       method: 'POST',
    //       body: {}
    //     })
    //     .then(response => {
    //       if (!response.ok) {
    //         throw new Error('Error al enviar la solicitud');
    //       }
    //       return response.json();
    //     })
    //     .then(data => {
    //       console.log('El registro ha sido creado:', data);
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    //   });