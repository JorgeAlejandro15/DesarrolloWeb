
 // setTimeout(() => {          // función para retrasar el delay de la pagina
 // }, 2000);

function add_producto() {
  // Agregar un HTML con un formulario de producto
  $( "#list_productos" ).append(`<div id="form" class="form-group">
  <div class="form-group pb-2 mt-2">
  <div class="input-group ">
  <input type="text" class="form-control" name="nombre_producto" id="productos" placeholder="Nombre del producto"
  pattern = "[a-zA-Z]+" oninvalid="event.target.setCustomValidity('El producto solo puede contener letras') ">  
  <button type="button" onclick="delete_rango(this)" class="btn btn-danger" aria-label="Left Align" style="padding-block:0px;"><strong>X</strong></button>
  </div>
  </div>`);
} 

function delete_rango(element) {
  $(element).parent().parent().remove(); 
}


// Función para mostrar una alerta al eliminar un item de la tabla
(function () {

  const btnEliminacion = document.querySelectorAll(".btnEliminacion");

        btnEliminacion.forEach(btn => {
         btn.addEventListener('click',(e)=>{
         
          e.preventDefault();

          const swalWithBootstrapButtons = Swal.mixin({
              customClass: {
              confirmButton: 'btn btn-success ms-2',
              cancelButton: 'btn btn-danger ms-2',
            },
              background: '#e1e6d3', 
              buttonsStyling: false
            })
            
            swalWithBootstrapButtons.fire({
              title: 'Atención!',     
              text: 'Desea eliminar al proveedor?',         
              icon: 'warning',
              showCancelButton: true,
              confirmButtonText: 'Aceptar',
              cancelButtonText: 'Cancelar',
              allowOutsideClick: () => false,
              allowEscapeKey: () => false,
              allowEnterKey: false,  
              showLoaderOnConfirm: true, 
              backdrop: true,
              reverseButtons: true
            })
            .then((result) => {                     //then es una función promesa
              if (result.isConfirmed) {                 
                  location.href = e.target.href;        // Operación para eliminar el item de la base de datos                           
              } 
              else if (         
                result.dismiss === Swal.DismissReason.cancel
              ) {
                swalWithBootstrapButtons.fire(
                  'Cancelado',
                  'El proveedor no se ha eliminado',
                  'error'
                )
              }
            })
        
      }); 
  });

})();  

// Función para crear la tabla dinámica en español  
$(document).ready(function () { 

  //Para traducir al español la data table
  
      const dataOptions={
          columnDefs:[
              {className:"centered", targets:[0,1,2,3,4,5,6]},
              {orderable:false, targets:[1,3,4,5,6]},
              {searchable:false, targets:[5,6]},
          ],
          pageLength:5,
          lengthMenu: [
              [5,10, 25, -1], 
              [5, 10, 25, 'Todos'],
          ],
          destroy:true,
          language: {
              "sProcessing":    "Procesando...",
              "sLengthMenu":    "Mostrar _MENU_ registros",
              "sZeroRecords":   "No se encontraron resultados",
              "sEmptyTable":    "Ningún dato disponible en esta tabla",
              "sInfo":          "Mostrando del _START_ al _END_ de un total de _TOTAL_ registros",
              "sInfoEmpty":     "Mostrando  0 de un total de 0 registros",
              /*"sInfoFiltered":  "(filtrado de un total de _MAX_ registros)",*/
              "sInfoFiltered":  "",
              "sInfoPostFix":   "",
              "sSearch":        "Buscar:",
              "sUrl":           "",
              "sInfoThousands":  ",",
              "sLoadingRecords": "Cargando...",
              "oPaginate": {
                  "sFirst":    "Primero",
                  "sLast":    "Último",
                  "sNext":    "Siguiente",
                  "sPrevious": "Anterior"
              },
              "oAria": {
                  "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                  "sSortDescending": ": Activar para ordenar la columna de manera descendente"
              }
          }
      };
  
      $('#datatable').DataTable(dataOptions);    
});


// Función para eliminar los productos
(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion2");
  
          btnEliminacion.forEach(btn => {
           btn.addEventListener('click',(e)=>{
           
            e.preventDefault();
  
            const swalWithBootstrapButtons = Swal.mixin({
                customClass: {
                confirmButton: 'btn btn-success ms-2',
                cancelButton: 'btn btn-danger ms-2',
              },
                background: '#e1e6d3', 
                buttonsStyling: false
              })
              
              swalWithBootstrapButtons.fire({
                title: 'Atención!',     
                text: 'Desea eliminar al producto?',         
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Aceptar',
                cancelButtonText: 'Cancelar',
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
                allowEnterKey: false,  
                showLoaderOnConfirm: true, 
                backdrop: true,
                reverseButtons: true
              })
              .then((result) => {                     //then es una función promesa
                if (result.isConfirmed) {                 
                    location.href = e.target.href;        // Operación para eliminar el item de la base de datos                           
                } 
                else if (         
                  result.dismiss === Swal.DismissReason.cancel
                ) {
                  swalWithBootstrapButtons.fire(
                    'Cancelado',
                    'El producto no se ha eliminado',
                    'error'
                  )
                }
              })
          
        }); 
    });
  
})(); 


   