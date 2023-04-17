function logear(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username != "" && password != "" && username !="admin") {
        document.getElementById('login-btn').style.display = 'none';
        document.getElementById('user-btn').style.display = 'block';        
    }
    else if(username != "" && password != "" && username =="admin"){
        window.location.href = "/administrador/";
    }
    else {
      alert("Nombre de usuario o contraseña incorrectos");
    }
}

function registrar(){
    window.location.href = "/registroUsuario/";
}

function perfil(){
    window.location.href = "/usuario/";
}

function validarMail(correoElectronico){
    var correoFormato = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}.){1,125}[A-Z]{2,63}$/i;
    if (!correoFormato.test(correoElectronico)){
        alert("Por favor ingrese una dirección de correo válida");
        return false;
    }
}

function guardar() {
    var nombreCompleto = document.getElementById("nombre").value;
    var correoElectronico = document.getElementById("correo").value;
    var claveIngreso = document.getElementById("clave").value;
    var repetirClave = document.getElementById("repetir-clave").value;
    var fechaNacimiento = document.getElementById("fecha-nacimiento").value;
    
    if (claveIngreso !== repetirClave) {
      alert("Las claves ingresadas no coinciden");
      return false;
    }

    if (nombreCompleto === "" || correoElectronico === "" || claveIngreso === "" || repetirClave === "" || fechaNacimiento ==="" ){
        alert("Favor completar todos los campos requeridos");
        return false;
    }
  
    validarMail(correoElectronico);

    var validarPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){6,18}$/;
    if (!validarPassword.test(claveIngreso)){
      alert("Por favor ingrese una contraseña/clave válida");
      return false; 
    }

    var anoNac = parseInt(fechaNacimiento.substring(0,4));
    var hoy = new Date();
    var anoActual = hoy.getFullYear();
    var edad = anoActual - anoNac;
    if (edad < 13) {
      alert("Debe tener al menos 13 años de edad para registrarse.");
      return false;
    }

    var usuario = {
        nombreCompleto: nombreCompleto,
        correoElectronico: correoElectronico,
        claveIngreso: claveIngreso,
        fechaNacimiento: fechaNacimiento,
        };

    var usuarioJSON = JSON.stringify(usuario);
        console.log(usuarioJSON);

    alert("Solicitud enviada, se enviara a su correo una copia");
}

function limpiar(){
        document.getElementById("nombre").value = "";
        document.getElementById("correo").value = "";
        document.getElementById("clave").value = "";
        document.getElementById("repetir-clave").value = "";
        document.getElementById("fecha-nacimiento").value = "";
}

function limpiarSolicitud(){
        document.getElementById("nombre").value = "";
        document.getElementById("correo").value = "";
        document.getElementById("telefono").value = "";
        document.getElementById("cantidad-personas").value = "";
        document.getElementById("flexCheckDefault").checked = false;
        document.getElementById("flexCheckChecked").checked = false;
        document.getElementById("descripcion").value = "";
        const checkboxs = document.querySelectorAll('input[type="checkbox"]:checked');
        checkboxs.forEach(checkbox => {checkbox.checked = false;
        });
}

function solicitarArriendo() {
  const nombre = document.getElementById("nombre").value;
  const correo = document.getElementById("correo").value;
  const telefono = document.getElementById("telefono").value;
  const cantidadPersonas = document.getElementById("cantidad-personas").value;
  const checkboxs = document.querySelectorAll('input[type="checkbox"]:checked');

  if (nombre === "" || correo === "" || telefono === "" || cantidadPersonas === "" || checkboxs.length === 0) {
    alert("Por favor complete todos los campos obligatorios");
    return false;
  }
    
  validarMail(correoElectronico);

}

function modificarUsuario() {
    let mailto = document.getElementById("mailto");
    var correoElectronico = document.getElementById("correo").value;
    var claveIngreso = document.getElementById("clave").value;
    var repetirClave = document.getElementById("repetir-clave").value;
    
    if (claveIngreso !== repetirClave) {
      alert("Las claves ingresadas no coinciden");
      return false;
    }

    if (correoElectronico === "" || claveIngreso === "" || repetirClave === ""){
        alert("Favor completar todos los campos requeridos");
        return false;
    }

    var correoFormato = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}.){1,125}[A-Z]{2,63}$/i;
    if (!correoFormato.test(correoElectronico)){
        alert("Por favor ingrese una dirección de correo válida");
        return false;
    }
    else{
        mailto.innerHTML = "Correo:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+correoElectronico;
        console.log(mailto);
    }

    var validarPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])([A-Za-z\d$@$!%*?&]|[^ ]){6,18}$/;
    if (!validarPassword.test(claveIngreso)){
      alert("Por favor ingrese una contraseña/clave válida");
      return false; 
    }

    var usuario = {
        correoElectronico: correoElectronico,
        claveIngreso: claveIngreso,
        };

    var usuarioJSON = JSON.stringify(usuario);
    console.log(usuarioJSON);

    alert("Datos modificados");
}

function recuperar() {
    var correoSolicitante = document.getElementById("correo").value;

    var correoFormato = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}.){1,125}[A-Z]{2,63}$/i;
    if (!correoFormato.test(correoSolicitante)){
        alert("Por favor ingrese una dirección de correo válida");
        return false;
    }

    alert("Correo enviado");
  }

function guardarSolicitud(){
    var nombreCompleto = document.getElementById("nombre").value;
    var correoElectronico = document.getElementById("correo").value;
    var TelefonoContacto = document.getElementById("telefono").value;
    var cantidadPersonas = document.getElementById("cantidad-personas").value;
    var flexCheckDefault = document.getElementById("flexCheckDefault").value;
    var flexCheckChecked = document.getElementById("flexCheckChecked").value;
    var descripcion = document.getElementById("descripcion").value;

    checkboxs.forEach(checkbox => {checkbox.checked = false;
      });

    if (nombreCompleto === "" || correoElectronico === "" || TelefonoContacto === "" || cantidadPersonas === "" || flexCheckDefault ==="" || flexCheckChecked ==="" || descripcion ==="" ){
        alert("Favor completar todos los campos requeridos");
        return false;
    }

    validarMail(correoElectronico);


    
}