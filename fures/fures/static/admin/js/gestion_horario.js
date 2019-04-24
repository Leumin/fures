
    $(document).ready(function () {
        var doc = $(document);
        $('a.add').die('click').live('click', function (e) {
            e.preventDefault();
            var content = $('#type-conta .type-row'),
                element = null;
            for (var i = 0; i < 1; i++) {
                element = content.clone();
                // var type_div = 'teams_' + $.now();
                // element.attr('id', type_div);
                // element.find('.remove-type').attr('targetDiv', type_div);
                // element.appendTo('#type_container');

                var type_div =  $.now();
                element.attr('id', type_div);
                element.find('.remove').attr('targetDiv', type_div);
                element.appendTo('#type_conta');

            }
        });

        $(".remove").die('click').live('click', function (e) {
            var didConfirm = confirm("Are you sure You want to delete");
            if (didConfirm == true) {
                // var id = $(this).attr('data-id');
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
