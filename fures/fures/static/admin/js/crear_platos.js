$(function () {
    $("#Nombre").keyup(function () {
        var This = $("#Nombre");
        var user = $("#Nombre").val();
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


    $("#precio").keyup(function () {
        var This = $("#precio");
        var user = $("#precio").val();
        var expre = /[^\d]/g;
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
});

        var regex = /[^.\d]/g;
          var numTel = document.getElementById("precio");
            numTel.addEventListener("keyup", function(){
            if (numTel.value == ""){
            numTel.value = "+";
            }
            numTel.value = numTel.value.replace(regex,"");
            })

// Example starter JavaScript for disabling form submissions if there are invalid fields
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
