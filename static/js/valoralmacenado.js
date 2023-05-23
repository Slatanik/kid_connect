

window.addEventListener('DOMContentLoaded', function() {
    var valorGuardado = localStorage.getItem("miDato");
    document.getElementById("storedValue").textContent = valorGuardado;
  });