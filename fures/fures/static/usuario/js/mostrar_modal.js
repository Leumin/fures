axios.get("/restaurante/")
    .then(function (res) {
        let modal = "";
        for (var i = 0; i < res.data.length; i++) {
            modal += `
       
                <h2 class="text-uppercase">${res.data[i].nombre}</h2>
                                <p class="item-intro text-muted">Lorem ipsum dolor sit amet consectetur.</p>
                                <img class="img-fluid d-block mx-auto"
                                     src="{% static 'usuario/img/portfolio/01-full.jpg' %}" alt="">
                                <p>Use this area to describe your project. Lorem ipsum dolor sit amet, consectetur
                                    adipisicing elit. Est blanditiis dolorem culpa incidunt minus dignissimos deserunt
                                    repellat aperiam quasi sunt officia expedita beatae cupiditate, maiores repudiandae,
                                    nostrum, reiciendis facere nemo!</p>
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
        elemento.innerHTML=modal;
    });


