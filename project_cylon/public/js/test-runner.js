$( document ).ready( function() {
    /// get project info ///
    request = $.ajax({
        url: "/api/project/info",
        type: "get",
        dataType: 'json'
    })
    .done( function(response) {
        $('#lbl_project').text(response.project);
    })
    .fail( function(jqXHR, textStatus, errorThrown){
        console.error("The following error occurred: " + textStatus, errorThrown);
    });
});

$('#btn_run').on('click', function() {
    $('#pnl_reports').text('Waiting...');

    $('#btn_run').attr('disabled', 'disabled');
    $('#btn_run').text('Running...');

    options = $('#txt_options').val();

    /// start run ///
    request = $.ajax({
        url: "/api/run/start",
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
        url: "/api/report/info",
        type: "get",
        dataType: 'json'
    })
    .done( function(response, textStatus, jqXHR) {
        if (response.files.length > 0) {
            $('#pnl_reports').text('');

            var path = response.path;
            for (i = 0; i < response.files.length; i++) {
                var filename = response.files[i].filename;
                var status = response.files[i].status;

                var color = {
                    "passed": "text-success",
                    "failed": "text-danger",
                    "skipped": "text-info"
                }[status];

                link = ' \
                <div class="row"> \
                  <div class="col-lg-8"> \
                    <a target="_blank" href="' + path + '/' + filename + '" class="btn btn-link" style="padding: 3px;">' + filename + '</a> \
                  </div> \
                  <div class="col-lg-4"> \
                    <div class="' + color + ' pull-right" style="padding: 3px">' + status + '</div> \
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
