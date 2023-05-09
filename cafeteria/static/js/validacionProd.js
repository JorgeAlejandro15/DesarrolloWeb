const $txtproducto = document.getElementById('producto'); 
const $formularioProve = document.getElementById('formularioProv2'); 



(function () {
    $formularioProve.addEventListener('submit', function(y) {
    const regex = /^[a-zA-Z\s]*$/;                              // Expresión regular para que reconozca solo letras
    let producto = String($txtproducto.value).trim();            //Para validar el nombre de los productos
 if (!producto.match(regex)) {
    y.preventDefault();                    
     Swal.fire({
        icon: 'error',
        background: '#e1e6d3',
        title: 'Error',
        text: 'El nombre solo puede contener letras'         
    })
   //alert("Error")
   }
});
})();


