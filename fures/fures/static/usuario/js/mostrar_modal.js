function dataUser(id) {
    axios.get("/restaurante/ver/" + id)
        .then(function (res) {
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
                                <button class="btn btn-primary" data-dismiss="modal" type="button">
                                    <!--<i class="fas fa-times"></i>-->
                                    Visitar
                                </button>
        `
            var elemento = document.getElementById('mostrar_modal');
            elemento.innerHTML = modal;
        });
}

