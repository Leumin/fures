axios.get(" ")
    .then(function (res) {
        let html = "";
        for (var i = 0; i < res.data.length; i++) {
            html += `
         
    <div class="padre">
        <div class="hijo">
            <h2 style="text-align:center">Nombre del Restaurante</h2>
            <!-- Container for the image gallery -->
            <div class="imgcontainer">

            <!-- Full-width images with number text -->
            <div class="mySlides">
                
                <img src="{% static 'usuario/img/slideshows/img_woods_wide.jpg' %}" style="width:100%">
            </div>

          

            <!-- Next and previous buttons -->
            <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
            <a class="next" onclick="plusSlides(1)">&#10095;</a>

        

            <!-- Thumbnail images -->
            <div class="row">
                <div class="column">
                    <img class="demo cursor" src="{% static 'usuario/img/slideshows/img_woods.jpg' %}" style="width:100%" onclick="currentSlide(1)" alt="">
                </div>
            
            </div>
        </div>

        </div>

    </div>

    <div class="container">
    <hr style="background-color: #e2e3e5">
    <div class="d-flex justify-content-around">
        <div class="row">
            <div class="col">
                <div class="media">
                    <img src="{% static 'usuario/img/servicios/parked-car.png' %}" width="20px">
                    <div class="media-body">

                            <!-- Button trigger modal -->
                            <button type="button" class="btn text-warning" data-toggle="modal" data-target="#exampleModal1" >
                               Ver Horarios
                            </button>

                            <!-- Modal -->
                            <div class="modal fade" id="exampleModal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="exampleModalLabel1">Horarios</h5>
                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div class="modal-body">
                                            <table class="table">

                                                <tbody>
                                                <tr>
                                                    <th scope="row">Lunes</th>
                                                    <td>11:00am-9:00pm</td>

                                                </tr>
                                              
                                                </tbody>
                                            </table>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn " data-dismiss="modal" style="background-color: #e60000 ; color: white">Close</button>
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
                    <img src="../img/services/placeholder.png" class="mr-3" alt="..." width="16px">
                    <div class="media-body">
                        <!-- Button trigger modal -->
                            <button type="button" class="btn text-warning" data-toggle="modal" data-target="#exampleModal">
                                Formas de Pago
                            </button>

                            <!-- Modal -->
                            <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                                <div class="modal-dialog" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="exampleModalLabel">Formas de Pago</h5>
                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div class="modal-body">
                                            <div class="col">
                                                <div class="media">
                                                    <img src="../img/services/016-money.png" class="mr-3" alt="...">
                                                    <div class="media-body">
                                                        <h5 class="mt-0">Tarjeta de Credito</h5>
                                                        <p>Master Card, Visa, Catracha.</p>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col">
                                                <div class="media">
                                                    <img src="..." class="mr-3" alt="...">
                                                    <div class="media-body">
                                                        <h5 class="mt-0">Tarjeta de Débito</h5>
                                                        <p>Catracha, Visa</p>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="col">
                                                <div class="media">
                                                    <img src="..." class="mr-3" alt="...">
                                                    <div class="media-body">
                                                        <h5 class="mt-0">Efectivo</h5>
                                                        <p>Dolar, Lempira</p>

                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn " data-dismiss="modal" style="background-color: #e60000 ; color: white" >Close</button>
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
                    <img src="../img/services/placeholder.png" class="mr-3" alt="..." width="16px">
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

    <div class="container">
    <hr style="background-color: #e2e3e5">
    <div class="row">
        <div class="col">
            <h6>Acerca de nuestro Restaurante</h6>
            <p>Esta es una breve descripción del restaurante y de los servicios que ofrecen, asi como información personalizada del restaurante. Esta es una breve descripción del restaurante y de los servicios que ofrecen, asi como información personalizada del restaurante.</p>

        </div>
    </div>
</div>

    <div class="container">
    <hr style="background-color: #e2e3e5">
    <h6>Servicios</h6>

<br>
    <div class="row">
        <div class="col">
            <div class="media">
                <img src="{% static 'usuario/img/servicios/parked-car.png' %}" class="mr-3" alt="..." width="20px">
                <div class="media-body">
                    <h6 class="mt-0">Media heading</h6>
                </div>
        </div>



    </div>

       

    </div>
</div>

    <div class="container">
    <hr style="background-color: #e2e3e5">
    <br>
    <div class="d-flex justify-content-center">
    <form>
        <div class="row">

            <div class="col">
                <input type='text' class="form-control" id='datetimepicker1' placeholder="Fecha de Reserva" style="width: 170px"/>
            </div>

            <div class="col">
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <label class="input-group-text" for="inputGroupSelect03">Personas</label>
                    </div>
                    <select class="custom-select" id="inputGroupSelect03" >
                        <option selected>Choose...</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </select>
                </div>
            </div>

            <div class="col">
                <button type="submit" class="btn btn-primary">Reservar</button>
            </div>
        </div>
    </form>
    </div>
    <br>
    <hr style="background-color: #e2e3e5">
<!--//////////////////////////-->

        <div class="d-flex justify-content-center">


    <div class="star_container">
        <h5>Rating</h5>

        <!--<h7>Click to rate:</h7>-->
        <div class='starrr' id='star1'></div>
        <div>&nbsp;
            <span class='your-choice-was' style='display: none; font-size: 15px'>
        Your rating was <span class='choice'></span>.
      </span>
        </div>

        <div class="form-group starrr">
            <label for="exampleFormControlTextarea1">Déjanos tu opinión</label>
            <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
            <button type="submit" class="btn btn-primary" style="margin-top: 20px">Enviar</button>
        </div>


    </div>

</div>
</div>
         
        `

        }

        var elemento = document.getElementById('restauranteinfo');
        elemento.innerHTML = html;
    });
