axios.get("/restaurante/")
    .then(function (res) {
        let html = "";
        for (var i = 0; i < res.data.length; i++) {
            html += `
        <div class="col-md-4 col-sm-6 portfolio-item">
                    <a class="portfolio-link" data-toggle="modal" href="#portfolioModal1">
                        <div class="portfolio-hover">
                            <div class="portfolio-hover-content">
                                <i class="fas fa-plus fa-3x"></i>
                            </div>
                        </div>
                        <img class="img-fluid" src="http://localhost:8000/templates/imagenes/${res.data[i].fields.imagen}" alt="imagen">
                    </a>
                    <div class="portfolio-caption">

                        <h4>${res.data[i].fields.nombre}</h4>

                    </div>
                </div>
        `

        }

        var elemento = document.getElementById('restaurantes_recientes');
        elemento.innerHTML=html;
    });


