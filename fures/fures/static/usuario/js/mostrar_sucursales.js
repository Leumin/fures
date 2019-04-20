function sucursales(id) {
    // location.href = "/sucursal/ver/";
    // console.log(id);
    axios.get("/sucursal/ver/" + id)
        .then(function (res) {
            console.log(res);
            let html = "";
            for (var i = 0; i < res.data.length; i++) {
                html += `
        <div class="col-md-4 col-sm-6 portfolio-item">
                    <a   class="portfolio-link" data-toggle="modal" data-target="#portfolioModal1">
                        <div class="portfolio-hover">
                            <div class="portfolio-hover-content">
                                <i class="fas fa-plus fa-3x"></i>
                            </div>
                        </div>
                        <img class="img-fluid" src="http://localhost:8000/media/${res.data[i].fields.imagen}" alt="imagen">
                    </a>
                    <div class="portfolio-caption">
         
                        <h4>${res.data[i].fields.direccion}</h4>
                        
                    </div>
                </div>
         
        `

            }
            var elemento = document.getElementById('restaurantes_recientes');
            elemento.innerHTML = html;
        });
}