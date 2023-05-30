class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session 
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():  
            self.carrito[id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,  
                'cantidad': 1,
                "acumulado": producto.precio, 
                'imagen': producto.imagen.url,
            }
        else:
            # for key , value in self.carrito.items():
                # if key == str(producto.id):
                #     value["cantidad"] = value["cantidad"] + 1
                #     value["acumulado"] = value["acumulado"] + str(producto.precio)   
                #     break
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio 
        self.guardar() 

    
    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    
    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.guardar()

    
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar()
        # for key,value in self.carrito.items():
        #     if key == str(producto.id):
        #             value["cantidad"] = value["cantidad"] - 1 
        #             if value["cantidad"] < 1:
        #                 self.eliminar(producto) 
        #             else:
        #                 value["acumulado"] = value["acumulado"] - str(producto.precio)  
        #                 self.guardar()  
        #             break
        #     else:
        #         print("No existe")


    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
