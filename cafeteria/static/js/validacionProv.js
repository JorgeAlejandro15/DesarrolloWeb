// Función para validar el formulario de registro
const $formularioProv = document.getElementById('formularioProv');   
const $txtnombre = document.getElementById('txtnombre');  
const $txtci = document.getElementById('txtci');
const $txtelefono = document.getElementById('txttelefono');
const $txtcorreo = document.getElementById('txtcorreo');

 

(function () {
    $formularioProv.addEventListener('submit', function(x) {  
     let nombre = String($txtnombre.value).trim();              //Función trim para quitar los espacios en blanco
     if (nombre.length===0) {
        x.preventDefault();      
       Swal.fire({
       icon: 'error',
       background: '#e1e6d3',
       title: 'Error',
       text: 'El nombre no puede estar vacío'      
       })     
   }

   let arregloN = String($txtnombre.value).split(" ");  
   for (let i = 0; i < arregloN.length; i++) {
    if (arregloN[i].charAt(0) != arregloN[i].charAt(0).toUpperCase()) {   // Condición para comprobar la mayúscula 
        x.preventDefault();
        Swal.fire({
            icon: 'error',
            background: '#e1e6d3',
            title: 'Error',
            text: 'El nombre debe empezar con mayúscula'       
            }) 
    }
   }
    
   const regex = /^[a-zA-Z\s]*$/;                      // Expresión regular para que reconozca solo letras

    if (!nombre.match(regex)) {
        x.preventDefault();
        Swal.fire({
            icon: 'error',
            background: '#e1e6d3',
            title: 'Error',
            text: 'El nombre solo puede contener letras'         
        })
    }
    
    const regExp = /^[0-9\s]*$/;                // expresión para controlar la entrada de números solamente
    let ci = String($txtci.value).trim();
    let telef = String($txtelefono.value).trim();
        if (!ci.match(regExp) || !telef.match(regExp)) { 
            x.preventDefault();
            Swal.fire({
                icon: 'error',
                background: '#e1e6d3',
                title: 'Error',
                text: 'El campo solo puede contener números de 0 a 9'          
            })
        }

    const regC = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let correo = String($txtcorreo.value).trim();
        if (!correo.match(regC)) {
            x.preventDefault();
            Swal.fire({
                icon: 'error',
                background: '#e1e6d3',
                title: 'Error',
                text: 'Correo incorrecto'          
            })
        }
       

});
})();

