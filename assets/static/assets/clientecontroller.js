app.controller('startApp', ['$scope', 'defaultService', function ($scope, defaultService) {
 console.log("start tienda");
 //$scope.id_usuario = $("#id_usuario").attr("value");
 $scope.servidor = "http://localhost:8000";
 $scope.tienda = $("#tienda").val();
 $scope.usuario_id = $("#usuario_id").val();
 
 if($scope.usuario_id == "None"){
 	
 }else{

 	defaultService.get('/service/cliente/detail/'+$scope.usuario_id+'/',function(d){
           console.log(d.pais)
           $scope.cliente = d;
           console.log($scope.cliente.pais);

        }, function (e){
        		console.log(e)
        	}
    );

 }



 $scope.cargar_productos_incluidos = function(categoria){
 	console.log("cargando productos" + categoria);
  $(".producto").css({"display":"block"});
  $(".detalle-producto").css({"display":"none"});
  $(".pago").css({"display":"none"});
 	defaultService.get('/tienda/productos/incluidos/?tienda='+$scope.tienda+'&categoria='+categoria,function(d){
           console.log(d)
           $scope.productos = d;    

        }, function (e){
        		console.log(e)
        	}
    );
 }

 $scope.autenticar_usuario = function(){
 	console.log($scope.correo+$scope.password);
 	defaultService.get('/login/autenticar/cliente/?usuario='+$scope.correo+'&password='+$scope.password,function(d){
           console.log(d);  
           if(d.codigo == '404') alert("Usuario o password incorrectos.")      
           else{
           	$("#login").css({"display":"none"});
           	
           	

           defaultService.get('/service/cliente/detail/'+d[0].usuario+'/',function(d){
           console.log(d.pais)
           $scope.cliente = d;
           $scope.msj_cliente = "Bienvenido "+$scope.correo;

		        }, function (e){
		        		console.log(e)
		        	}
		    );



           	

           }
        }, function (e){
        		console.log(e)
        	}
    );
 }


  $scope.comprar = function(id){

  	for(var i in $scope.productos){
  		if($scope.productos[i].id == id){
  			$scope.producto_seleccionado = $scope.productos[i];
  		}
  	}
   $(".detalle-producto").css({"display":"block"});
   $(".pago").css({"display":"block"});
   $(".producto").css({"display":"none"});
  
 }






 }]);