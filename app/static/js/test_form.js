$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#target_start').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $('#target_start_test').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $('#target_end').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $('#target_end_test').datetimepicker({
        format: 'YYYY-MM-DD',
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });


});