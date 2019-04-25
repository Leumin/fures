$(function () {
    $("#nombre_persona").keyup(function () {
        var This = $("#nombre_persona");
        var user = $("#nombre_persona").val();
        var expre = /^[a-zA-z]+$/;
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 2px solid #F00');
        } else {
            This.attr('style', 'border: 2px solid #0F0');
        }

        if (valido) {
            This.attr('style', 'border: 2px solid #0F0');
        } else {
            This.attr('style', 'border: 2px solid #F00');
        }
    });

    $("#apellido_persona").keyup(function () {
        var This = $("#apellido_persona");
        var user = $("#apellido_persona").val();
        var expre = /^[a-zA-z]+$/;
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 1px solid #F00');
        } else {
            This.attr('style', 'border: 1px solid #0F0');
        }

        if (valido) {
            This.attr('style', 'border: 1px solid #0F0');
        } else {
            This.attr('style', 'border: 1px solid #F00');
        }
    });


    $("#inputDirección").keyup(function () {
        var This = $("#inputDirección");
        var user = $("#inputDirección").val();
        var expre = /^[a-zA-z]+$/;
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 1px solid #F00');
        } else {
            This.attr('style', 'border: 1px solid #0F0');
        }

        if (valido) {
            This.attr('style', 'border: 1px solid #0F0');
        } else {
            This.attr('style', 'border: 1px solid #F00');
        }
    });

    $("#inputNombreUsuario").keyup(function () {
        var This = $("#inputNombreUsuario");
        var user = $("#inputNombreUsuario").val();
        var expre = /^[a-zA-z]+$/;
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 1px solid #F00');
        } else {
            This.attr('style', 'border: 1px solid #0F0');
        }

        if (valido) {
            This.attr('style', 'border: 1px solid #0F0');
        } else {
            This.attr('style', 'border: 1px solid #F00');
        }
    });

    $("#inputPassword4").keyup(function () {
        var This = $("#inputPassword4");
        var user = $("#inputPassword4").val();
        var expre = /^[a-zA-z]+$/;
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 1px solid #F00');
        } else {
            This.attr('style', 'border: 1px solid #0F0');
        }

        if (valido) {
            This.attr('style', 'border: 1px solid #0F0');
        } else {
            This.attr('style', 'border: 1px solid #F00');
        }
    });

    $("#inputNumero").keyup(function () {
        var This = $("#inputNumero");
        var user = $("#inputNumero").val();
        var re = /^[0-9]$/;
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 1px solid #F00');
        } else {
            This.attr('style', 'border: 1px solid #0F0');
        }

        if (valido) {
            This.attr('style', 'border: 1px solid #0F0');
        } else {
            This.attr('style', 'border: 1px solid #F00');
        }
    });

    $("#inputCorreo").keyup(function () {
        var This = $("#inputCorreo");
        var user = $("#inputCorreo").val();
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 1px solid #F00');
        } else {
            This.attr('style', 'border: 1px solid #0F0');
        }

        if (valido) {
            This.attr('style', 'border: 1px solid #0F0');
        } else {
            This.attr('style', 'border: 1px solid #F00');
        }
    });

    $('#inputCorreo').keyup(function () {
        var _this = $('#inputCorreo');
        var _email = $('#inputCorreo').val();
        var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        var valid = re.test(_email);

        if (valid) {
            _this.attr('style', 'background:white');
        } else {
            _this.attr('style', 'background:#FF4A4A');
        }
    });
        var regex = /[^\d]/g;
          var numTel = document.getElementById("inputNumero");
            numTel.addEventListener("keyup", function(){
            if (numTel.value == ""){
            numTel.value = "+";
            }
            numTel.value = numTel.value.replace(regex,"");
            })


});