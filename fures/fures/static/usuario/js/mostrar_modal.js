function dataUser(nombre) {
    axios.get("/restaurante/?nombre="+nombre)
        .then(function (res) {
            let modal = "";
            for (var i = 0; i < res.data.length; i++) {
                modal += `
       
                <h2 class="text-uppercase">${res.data[i].fields.nombre}</h2>
                                <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p>
                                <img class="img-fluid d-block mx-auto"
                                     src="{% static 'usuario/img/portfolio/01-full.jpg' %}" alt="">
                                <p>${res.data[i].fields.descripcion}</p>
                                <ul class="list-inline">
                                    <li>Date: January 2017</li>
                                    <li>Client: Threads</li>
                                    <li>Category: Illustration</li>
                                </ul>
                                <button class="btn btn-primary" data-dismiss="modal" type="button">
                                    <!--<i class="fas fa-times"></i>-->
                                    Visitar
                                </button>
        `

            }

            var elemento = document.getElementById('mostrar_modal');
            elemento.innerHTML = modal;
        });
}

