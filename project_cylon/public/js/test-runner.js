$( document ).ready( function() {
    /// get project info ///
    request = $.ajax({
        url: "/info",
        type: "get",
        dataType: 'json'
    })
    .done( function(response, textStatus, jqXHR) {
        $('#lbl_project').text(response.project);
    })
    .fail(function(jqXHR, textStatus, errorThrown){
        console.error("The following error occurred: " + textStatus, errorThrown);
    });

    displayReports();
});

$('#btn_run').on('click', function() {
    $('#pnl_reports').text('Waiting...');

    $('#btn_run').attr('disabled', 'disabled');
    $('#btn_run').text('Running...');

    options = $('#txt_options').val();

    /// start run ///
    request = $.ajax({
        url: "/run",
        type: "get",
        data: {
            "options": options
        }
    })
    .done( function(response, textStatus, jqXHR) {
        $('#btn_run').text('Run');
        $('#btn_run').removeAttr('disabled');

        //generateReports();
        displayReports();
    })
    .fail(function (jqXHR, textStatus, errorThrown){
        console.error("The following error occurred: " + textStatus, errorThrown);
    });
});


// function generateReports() {
//     request = $.ajax({
//         url: "/gen_reports",
//         type: "get"
//         //dataType: 'json'
//     })
//     .done( function(response, textStatus, jqXHR) {
//     });
// }

function displayReports() {
    request = $.ajax({
        url: "/reports",
        type: "get",
        dataType: 'json'
    })
    .done( function(response, textStatus, jqXHR) {
        if (response.files.length > 0) {
            $('#pnl_reports').text('');

            for (i = 0; i < response.files.length; i++) {
                filepath = response.path;
                filename = response.files[i];
                link = ' \
                <div class="row"> \
                  <div class="col-lg-8"> \
                    <a href="' + filepath + '/' + filename + '" class="btn btn-link" style="padding: 3px;">' + filename + '</a> \
                  </div> \
                  <div class="col-lg-4"> \
                    <div class="text-success pull-right" style="padding: 3px"></div> \
                  </div> \
                </div>';

                $('#pnl_reports').append(link);
            }
        }
    });
}


/// tmp timer ///
/*$('#btn_timer').on('click', function() {
    if (tm.isStarted) {
        tm.stop();
    }
    else {
        tm.start();
    }
});


function Timer() {
    timer = null;
    this.isStarted = false;

    this.fncall = {};
    this.interval = 5000;

    this.start = function() {
        timer = setInterval(this.fncall, this.interval);
        this.isStarted = true;
    };

    this.stop = function() {
        clearInterval(timer);
        this.isStarted = false;
    };
}

tm = new Timer();
tm.interval = 3000;
tm.fncall = function() {
    request = $.ajax({
        url: "/getlog",
        type: "get"
    })
    .done( function (response, textStatus, jqXHR) {
        console.log(response.toString());
    });
};*/

//tm.start();
