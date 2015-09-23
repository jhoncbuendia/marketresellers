/**
 * Created by jhon on 24/01/15.
 */
app.controller('startApp', ['$scope', 'defaultService', function ($scope, defaultService) {
 console.log("start");
 $scope.id_usuario = $("#id_usuario").attr("value");
 $scope.servidor = "http://localhost:8000";
 //$scope.servidor = "http://54.200.219.177:8000";
 console.log("id usuario:"+$scope.id_usuario); 

    
}]);


app.controller('perfil', ['$scope', 'defaultService', function ($scope, defaultService) {
 console.log("cargando perfil");
 $scope.cargar_perfil = function(){
 	defaultService.get('/service/perfil/detail/'+$scope.id_usuario+'/',function(d){
           //console.log(d)
           $scope.titular_cuenta = d.Titular_cuenta_bancaria;
           $scope.pais = d.pais;
           $scope.ciudad = d.ciudad;
           $scope.banco = d.banco;
           $scope.numero_cuenta = d.numero_cuenta;
           //alert($scope.titular_cuenta);
        }, function (e){console.log(e)
    });

 }

    $scope.cargar_perfil();

    $scope.modificar_perfil = function(){
    	var data = {
    		"Titular_cuenta_bancaria": $scope.titular_cuenta,
		    "banco": $scope.banco ,
		    "numero_cuenta": $scope.numero_cuenta,
		    "pais": $scope.pais,
		    "ciudad": $scope.ciudad
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
    
  

    defaultService.get('/service/tienda/list/',function(d){
           console.log("linea 19 cargando perfil");
           $scope.tiendas = d;
          
        }, function (e){console.log(e)
    });


    $scope.btn_tiendas = function(){
    	console.log("linea 27 btn_tiendas")
    	defaultService.get('/service/perfil/detail/'+$scope.id_usuario+'/',function(data){
					           
					           $scope.tiendas_incluidas = data.tienda;     
					          
					        }, function (e){console.log(e)
					    });
    }



    $scope.incluir_tienda = function(id){
    	//alert(id);
    	var tiendas = [];
    	defaultService.get('/service/perfil/detail/'+$scope.id_usuario+'/',function(d){
           
           tiendas = d.tienda;

           if(tiendas.length == 0){
           	tiendas[0] = id;
           	defaultService.put('/service/perfil/detail/'+$scope.id_usuario+'/', d ,function(data){
					          console.log("linea 48 incluyendo tiendas");      
					           defaultService.get('/service/perfil/detail/'+$scope.id_usuario+'/',function(data){
					           
					           $scope.tiendas_incluidas = data.tienda;     
					          
							        }, function (e){console.log(e)
							    });
					          
					        }, function (e){console.log(e)
					    });

           }
           else{
           		for ( var i in d.tienda){
           	
	           		if( d.tienda[i] != id )  {
	           			tiendas[tiendas.length] = id;
	           			d.tienda = tiendas;
	           			defaultService.put('/service/perfil/detail/'+$scope.id_usuario+'/', d ,function(data){
					           //console.log(data); 
					           defaultService.get('/service/perfil/detail/'+$scope.id_usuario+'/',function(data){
					           	//console.log(data);
					           	$scope.tiendas_incluidas = data.tienda;     
					          
							        }, function (e){console.log(e)
							    });       
					          
					        }, function (e){console.log(e)
					    });

	           		}
	           		else {
	           			console.log("linea 80 esta tienda ya se encuentra incluida");
	           		}
           		}

           }


           

           
           
          
        }, function (e){console.log(e)
    });
    	

    }



    $scope.excluir_tienda = function(id){
    	console.log("linea 101 excluyendo tiendas");
    	defaultService.get('/service/perfil/detail/'+$scope.id_usuario+'/',function(data){
					           	console.log(data);
					           	var tiendas_incluidas = [];  

					           	for(var i in data.tienda) {
					           		if(data.tienda[i] == id){
					           			console.log("linea 110 excluyendo tienda: "+ id)
					           		}
					           		else{
					           			tiendas_incluidas[tiendas_incluidas.length] = data.tienda[i];
					           		}
					           	} 

					           	//console.log(tiendas_incluidas);

					           	data.tienda = tiendas_incluidas;

					           	defaultService.put('/service/perfil/detail/'+$scope.id_usuario+'/', data ,function(d){
							               
							           defaultService.get('/service/perfil/detail/'+$scope.id_usuario+'/',function(data2){
							           //console.log(data2);
							           $scope.tiendas_incluidas = data2.tienda;     
							          
									        }, function (e){console.log(e)
									    });
							          
							        }, function (e){console.log(e)
							    });



					          
							        }, function (e){console.log(e)
							    });
    }



    $scope.generar_links = function(){
    	//alert("generando links");
    	var links = new Array();
    	var tiendas = $scope.tiendas;
    	var tiendas_incluidas = $scope.tiendas_incluidas;

    	console.log(tiendas);
    	console.log(tiendas_incluidas);

    	for (  var i in tiendas){
    		//console.log(tiendas[i].id)
    		for(var j in tiendas_incluidas){
    			if(tiendas_incluidas[j] == tiendas[i].id ){
    				//console.log(tiendas[i]);
    				links.push(tiendas[i]);
    			}
    		}
    	}
    	$scope.links = links;
    	console.log(links);
    }

    $scope.go_tienda = function(){
    	var correo = $("#correo").val();
    	var vendedora = $("#vendedora").val();
    	var tienda = $("#tienda").val();

    	var url = $scope.servidor+'/nuevo/cliente/?correo='+correo+'&vendedora='+vendedora+'&tienda='+tienda;
    	window.location = url;
    	//alert(url);
    }


    $scope.btn_clientes = function(){
    	

    	defaultService.get('/service/cliente/detail/'+$scope.id_usuario+'/',function(data){
							           //console.log(data2);
							           $scope.clientes = data; 
							           console.log($scope.clientes);
							            $('.facturacion').css('display', 'none');
    									$('.tiendas').css('display', 'none');
								    	$('.ventas').css('display', 'none');
								    	$('.clientes').css('display', 'block');    
							          
									        }, function (e){console.log(e)
									    });


    }

}]);