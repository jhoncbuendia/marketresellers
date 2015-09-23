/**
 * Created by jhon on 24/01/15.
 */
app.controller('startApp', ['$scope', 'defaultService', function ($scope, defaultService) {
 console.log("start tienda");
 //$scope.id_usuario = $("#id_usuario").attr("value");
 $scope.servidor = "http://localhost:8000";
 $scope.tienda = $("#tienda").val();
 $scope.id_usuario = $("#id_usuario").val();
 //$scope.servidor = "http://54.200.219.177:8000";
 //console.log("id usuario:"+$scope.id_usuario);

$scope.cargar_productos = function(categoria){
  $("#productos").css({"display":"block"});
      $("#perfil").css({"display":"none"});
 	console.log("cargando productos" + categoria);
 	defaultService.get('/service/producto/list/'+categoria+'/',function(d){
           console.log(d)
           $scope.productos = d;          
        }, function (e){console.log(e)
    });
 }


 $scope.cargar_productos_incluidos = function(categoria){
 	console.log("cargando productos" + categoria);
  $(".producto").css({"display":"block"});
  $(".detalle-producto").css({"display":"none"});
  $(".pago").css({"display":"none"});
 	defaultService.get('/tienda/productos/incluidos/?tienda='+$scope.tienda+'&categoria='+categoria,function(d){
           console.log(d)
           $scope.productos = d;    

        }, function (e){console.log(e)
    });
 }

 $scope.comprar = function(id){
  $(".detalle-producto").css({"display":"block"});
  $(".pago").css({"display":"block"});
   $(".producto").css({"display":"none"});
  
 }

 $scope.incluir_producto = function(id){
 	
 	//alert(id+$scope.tienda);
 	defaultService.get('/service/tienda/detail/'+$scope.tienda+'/',function(d){
          
            var productos = d.productos;   
            
            var flag = true;
            for(var p in productos){
            	if (id == productos[p])
            	{
            		alert("producto ya incluido")
            		flag = false;
            	}

            	
            }

            if(flag){
            	
                               
                productos.push(id);
                d.productos = productos;

                //console.log(d);
                 
           //alert($scope.titular_cuenta);
           defaultService.put('/service/tienda/detail/'+$scope.tienda+'/',d,function(data){
                   console.log(data)
                   alert("Producto includo con exito");
                }, function (e){console.log(e)
            });
                
                
            }

        }, function (e){console.log(e)
    });

 }


  $scope.modificar_perfil = function(){
      var data = {
        "usuario": $scope.id_usuario,
        "tienda": $scope.tienda, 
        "Titular_cuenta_bancaria": $("#titular_cuenta").val(),
        "banco": $("#banco").val(),
        "numero_cuenta": $("#numero_cuenta").val(),
        "pais": $("#pais").val(),
        "ciudad": $("#ciudad").val()
      };
         
           console.log(data);
           //alert($scope.titular_cuenta);
           defaultService.put('/service/perfil/detail/'+$scope.id_usuario+'/',data,function(d){
           console.log(d)
           $scope.titular_cuenta = d.Titular_cuenta_bancaria;
           $scope.pais = d.pais;
           $scope.ciudad = d.ciudad;
           $scope.banco = d.banco;
           $scope.numero_cuenta = d.numero_cuenta;
           alert("Datos modificados con exito");
        }, function (e){console.log(e)
    });
        

      
    }

    $scope.editar_perfil = function(){
      $("#productos").css({"display":"none"});
      $("#perfil").css({"display":"block"});
    }


  $scope.excluir_producto = function(id){
    
    //alert(id+$scope.tienda);
    defaultService.get('/service/tienda/detail/'+$scope.tienda+'/',function(d){
          
            var productos = d.productos;   
            var aux = [];
            var flag = true;
            for(var p in productos){
                if (id == productos[p])
                {
                    //alert("producto encontado"+productos[p])
                   
                }
                else{
                    aux.push(productos[p]);
                }

                
            }

            console.log(aux);
                               
                
                d.productos = aux;

                //console.log(d);
                 
           //alert($scope.titular_cuenta);
           defaultService.put('/service/tienda/detail/'+$scope.tienda+'/',d,function(data){
                   console.log(data)
                   alert("Producto excluido con exito");

                }, function (e){console.log(e)
            });
                
                
            

        }, function (e){console.log(e)
    });

 }
 

    
}]);

