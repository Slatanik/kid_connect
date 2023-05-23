/*fichaalumnoJS*
const form = document.getElementById('miFormulario');
print="quepaso"
form.addEventListener('submit', function(event) {
event.preventDefault(); // Evita que la página se recargue al enviar el formulario

const datos = new FormData(form); // Obtiene los datos del formulario

fetch('http://tmp.enred.cl/kc/rest/post_ficha.php', {
method: 'POST',
body: {}
})
.then(response => {
if (!response.ok) {
throw new Error('Error al enviar la solicitud');
}
return response.json();
})
.then(data => {
console.log('El registro ha sido creado:', data);
})
.catch(error => {
console.error(error);
});
});*/
