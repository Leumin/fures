$(function () {
    $("#Direccion").keyup(function () {
        var This = $("#Direccion");
        var user = $("#Direccion").val();
        var expre = /^[a-zA-z1-9._,:"'-]+$/;
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

    $("#telefono").keyup(function () {
        var This = $("#telefono");
        var user = $("#telefono").val();
        var valido = valido.test(user);
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

        $("#Capacidad").keyup(function () {
        var This = $("#Capacidad");
        var user = $("#Capacidad").val();
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

    $("#AcercaDe").keyup(function () {
        var This = $("#AcercaDe");
        var user = $("#AcercaDe").val();
        var expre = /^[a-zA-z]+$/;
        var valido = expre.test(user);
        if (user == "" || user == null) {
            This.attr('style', 'border: 2px solid #F00');
        } else {
            This.attr('style', 'border: 2px solid #0F0');
        }


        var regex = /[^\d]/g;
          var numTel = document.getElementById("telefono");
            numTel.addEventListener("keyup", function(){
            if (numTel.value == ""){
            numTel.value = "+";
            }
            numTel.value = numTel.value.replace(regex,"");
            })



    (function() {
        'use strict';
        window.addEventListener('load', function() {
            // Fetch all the forms we want to apply custom Bootstrap validation styles to
            var forms = document.getElementsByClassName('needs-validation');
            // Loop over them and prevent submission
            var validation = Array.prototype.filter.call(forms, function(form) {
                form.addEventListener('submit', function(event) {
                    if (form.checkValidity() === false) {
                        event.preventDefault();
                        event.stopPropagation();
                    }
                    form.classList.add('was-validated');
                }, false);
            });
        }, false);
     })();
});