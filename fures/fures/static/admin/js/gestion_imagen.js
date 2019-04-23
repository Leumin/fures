$(document).ready(function () {
        var doc = $(document);
        $('a.add-type').die('click').live('click', function (e) {
            e.preventDefault();
            var content = $('#type-container .type-row'),
                element = null;
            for (var i = 0; i < 1; i++) {
                element = content.clone();
                var type_div = 'teams_' + $.now();
                element.attr('id', type_div);
                element.find('.remove-type').attr('targetDiv', type_div);
                element.appendTo('#type_container');

            }
        });

        $(".remove-type").die('click').live('click', function (e) {
            var didConfirm = confirm("Está seguro de que quiere borrar ésta imagen?");
            if (didConfirm == true) {
                var id = $(this).attr('data-id');
                var targetDiv = $(this).attr('targetDiv');
                //if (id == 0) {
                //var trID = jQuery(this).parents("tr").attr('id');
                $('#' + targetDiv).remove();
                // }
                return true;
            } else {
                return false;
            }
        });

    });