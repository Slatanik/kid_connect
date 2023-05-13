function guardarValor() {
    var valor = document.getElementById("myInput").value;
    localStorage.setItem("miDato", valor);
    alert("Valor guardado en localStorage");
  }