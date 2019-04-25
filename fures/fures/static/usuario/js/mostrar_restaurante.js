var actual = window.location + '';
var split = actual.split("/");
var id = split[split.length - 1];


Promise.all([axios.get("/sucursal/ver/sucursal/" + id), axios.get("/sucursal/imagen/" + id), axios.get("/sucursal/horario/" + id), axios.get("/sucursal/platos/"+id)])
    .then(([suc, img, hor, menu]) => {
        let html = "";
        html += `
 
    <div class="padre">
        <div class="hijo">
            <h2 style="text-align:center">${Object.values(suc.data)[4]}</h2>
            <!-- Container for the image gallery -->
            <div class="imgcontainer">
     `;
        <!-- Full-width images with number text -->
        for (var i = 0; i < img.data.length; i++) {
            html += `
                <div class="mySlides" >
                    <img src="http://localhost:8000/media/${img.data[i].fields.imagen}"  onload="currentSlide(1)" style="width:1200px; height: 617px">
                </div>
              `
        }

        html += `
                <!-- Next and previous buttons -->
                <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
                <a class="next" onclick="plusSlides(1)">&#10095;</a>
                <div class="row">
            `;


        <!-- Thumbnail images -->
        for (var i = 0; i < img.data.length; i++) {
            html += `
                    <div class="column">
                        <img class="demo cursor" src="http://localhost:8000/media/${img.data[i].fields.imagen}" style="width:200px; height: 152px" onclick="currentSlide(${i + 1})" alt="">
                    </div> 
             `
        }

        html += `
                </div>
            </div>
         </div>
    </div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
            <div class="container">
            <hr style="background-color: #e2e3e5">
            <div class="d-flex justify-content-around">
                <div class="row">
                    <div class="col">
                        <div class="media">
                            <img src="http://localhost:8000/media/iconos/time.png" width="20px">
                            <div class="media-body">

                                <!-- Button trigger modal -->
                                <button type="button" class="btn text-warning" data-toggle="modal"
                                        data-target="#exampleModal1">
                                    Ver Horarios
                                </button>

                                <!-- Modal -->
                                <div id="horario">
                                    <div class="modal fade" id="exampleModal1" tabindex="-1" role="dialog"
                                         aria-labelledby="exampleModalLabel" aria-hidden="true">
                                        <div class="modal-dialog" role="document">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h5 class="modal-title" id="exampleModalLabel1">Horarios</h5>
                                                    <button type="button" class="close" data-dismiss="modal"
                                                            aria-label="Close">
                                                        <span aria-hidden="true">&times;</span>
                                                    </button>
                                                </div>
                                                <div class="modal-body">
                                                    <table class="table">
                
                                                        <tbody>
                `;
        for (var i = 0; i < hor.data.length; i++) {
            html += `
                                                        <tr>
                                                            <th scope="row">${hor.data[i].fields.dia}</th>
                                                            <td>${hor.data[i].fields.hora_inicio}-${hor.data[i].fields.hora_cierre}</td>
                                                        <tr>
            `;
        }

        html += `
                                                        </tbody>
                                                    </table>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn " data-dismiss="modal"
                                                            style="background-color: #e60000 ; color: white">Close
                                                    </button>
                                                    <!--<button type="button" class="btn btn-primary">Save changes</button>-->
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="media">
                            <img src="http://localhost:8000/media/iconos/031-menu-1.png" class="mr-3" alt="..." width="25px">
                            <div class="media-body">
                                 
                                <button type="button" class="btn text-warning" data-toggle="modal"
                                        data-target="#exampleModal">
                                    Menu
                                </button>

                                <!-- Modal -->
                                <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog"
                                     aria-labelledby="exampleModalLabel" aria-hidden="true">
                                    <div class="modal-dialog modal-xl" role="document">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <button type="button" class="close" data-dismiss="modal"
                                                        aria-label="Close">
                                                    <span aria-hidden="true">&times;</span>
                                                </button>
                                            </div>
                                            
                                            `;
        html += ` 
            <div class="modal-body">
            <div class="row justify-content-center">
                <h1>Menu</h1>
            </div>
                <div class="row justify-content-center" style="height: 750px; overflow-y: scroll">
        `;
        for (var i = 0; i < menu.data.length; i++) {
            html += `
                    <div class="col-4 justify-content-center">
                        <img class="row justify-content-center" src="http://localhost:8000/media/restaurantes/8c4db76b5cf595b1715ae1a45a13dafb.jpg" alt="..." style="width: 100%; height: 180px">
                        <hr>
                        <div class="media-body">
                            <div class="row justify-content-center">
                               <h2 class="mt-0">${menu.data[i].fields.nombre_plato}</h2>
                            </div>
                            <div class="row">
                                    <div class="col"><h5>Precio:</h5></div>
                                    <div class="col"></div>
                                    <div class="col"><h5>L. ${menu.data[i].fields.precio}</h5></div>
                            </div>
                        </div>
                        <hr>
                    </div> 
               
             `;
        }
        html += `
                                            <div class="row modal-footer">
                                                <!--<button type="button" class="btn btn-primary">Save changes</button>-->
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="media">
                            <img src="http://localhost:8000/media/iconos/014-placeholder.png" class="mr-3" alt="..." width="25px">
                            <div class="media-body">
                                <h6 class="mt-0">Ubicacion</h6>
                                <address>
                                    Col. Sitramacsa, calle del IHSS , una cuadra adentro
                                </address>
                                <a href="#">Cómo llegar</a>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    

`;
        var elemento = document.getElementById('restauranteinfo');
        elemento.innerHTML = html;

    });



