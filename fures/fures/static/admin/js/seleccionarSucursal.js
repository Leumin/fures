
axios.get("sucursal/ver/admin/")
    .then(function (res) {
        console.log(res);
        let html = "";

        html += `
                <label>Seleccione Sucursal</label>
                    <select class="custom-select" required>
                        <option selected>Selecione la sucursal</option>
               `;
        for (var i = 0; i < res.data.length; i++) {
            html += `
                        <option value="${res.data[i].pk}">${res.data[i].fields.direccion}</option>     
                  `;}
            html += `
                    </select>
                    <br>
                    <br>

        `



        var elemento = document.getElementById('desplegar');
        elemento.innerHTML = html;
    });
