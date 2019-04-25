axios.get("/restaurante/ultimos")
    .then(function (res) {
        let html = "";
        for (var i = 0; i < res.data.length; i++) {
            html += `
        <div class="col-md-4 col-sm-6 portfolio-item">
                    <a id="restaurante" class="portfolio-link" data-toggle="modal" data-target="#portfolioModal1" onclick="dataUser('${res.data[i].pk}')">
                        <div class="portfolio-hover">
                            <div class="portfolio-hover-content">
                                <i class="fas fa-plus fa-3x"></i>
                            </div>
                        </div>
                        <img class="img-fluid" src="http://localhost:8000/media/${res.data[i].fields.imagen}" alt="imagen" style="width:350px; height: 200px ">
                    </a>
                    <div class="portfolio-caption">
      
                        <h4>${res.data[i].fields.nombre}</h4>
                        <p class="text-muted">Illustration</p>
                    </div>
                </div>
         
        `

        }

        var elemento = document.getElementById('restaurantes_recientes')
        elemento.innerHTML = html;
    });
