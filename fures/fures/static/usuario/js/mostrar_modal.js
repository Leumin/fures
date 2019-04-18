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
                                <a data-target="#portfolioModal2" class="btn btn-primary" data-dismiss="modal" type="button">
                                    <!--<i class="fas fa-times"></i>-->
                                    Visitar
                                </a>
                                <h4 class="section-heading text-uppercase">Sucursales</h4>
                        `;
            for (var i = 0; i < suc.data.length; i++) {
                 modal += `
                          <div>
                            <div class="row" id="restaurantes_recientes">
                                <div class="col-md-4 col-sm-6 portfolio-item">
                                    <a class="portfolio-link" data-toggle="modal" href="#portfolioModal1">
                                        <div class="portfolio-hover">
                                            <div class="portfolio-hover-content">
                                                <i class="fas fa-plus fa-3x"></i>
                                            </div>
                                        </div>
                                        <img class="img-fluid" src="" alt="">
                                    </a>
                                    <div class="portfolio-caption">
                                        <h4></h4>
                                        <p class="text-muted">${suc.data[i].fields.direccion}</p>
                                    </div>
                                </div>
                          </div>
                 `
            }
            var elemento = document.getElementById('mostrar_modal');
            elemento.innerHTML = modal;
        });
}
