function dataUser(id) {
    Promise.all([axios.get("/restaurante/ver/"+ id), axios.get("/sucursal/ver/"+id)])
        .then(([res, suc]) => {
            console.log(suc);
            let modal = "";
            modal += `
                <h2 class="text-uppercase">${Object.values(res.data)[1]}</h2>
<!--                                <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p>-->
                                <img class="img-fluid d-block mx-auto"
                                     src="http://localhost:8000/media/${Object.values(res.data)[3]}" alt="">
                                    
                                <p>${Object.values(res.data)[2]}</p>
                                <ul class="list-inline">
<!--                                    <li>Date: January 2017</li>-->
<!--                                    <li>Client: Threads</li>-->
                                    <li>Category: Illustration</li>
                                </ul>
                                
                                <h4 class="section-heading text-uppercase">Sucursales</h4>
                        `;


            for (var i = 0; i < suc.data.length; i++) {
                 modal += `

<!--    <h5 class="card-title">${suc.data[i].fields.direccion}</h5>-->



 <div class="container">
                    <div class="row">
                        <div class="col-lg-8 mx-auto">
                            <div class="modal-body" id="mostrar_modal">  
                            <div class="card">
  
  <div class="card-body">
    <h5 class="card-title">${suc.data[i].fields.direccion}</h5>
    <h6 class="card-title">${suc.data[i].fields.telefono}</h6>
<!--    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>-->
    <a href="#" class="btn btn-primary" onclick="">Visitar</a>
  </div>
</div>
                            </div>
                        </div>    
                    </div>        
 </div>   
                 `
            }
            var elemento = document.getElementById('mostrar_modal');
            elemento.innerHTML = modal;
        });
}
