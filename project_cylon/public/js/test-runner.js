$( document ).ready( function() {
    /// get project info ///
    // request = $.ajax({
    //     url: "/api/project/info",
    //     type: "get",
    //     dataType: 'json'
    // })
    // .done( function(response) {
    //     $('#lbl_project').text(response.project);
    // })
    // .fail( function(jqXHR, textStatus, errorThrown){
    //     console.error("The following error occurred: " + textStatus, errorThrown);
    // });

    // console.log('show test report');
    // var report = new TestReport();
    // report.getInfo();
    // report.renderHead();
    // report.renderBody();
    //
    // var output = new ConsoleOutput();
    // output.getInfo();
    // output.render();

    //var runPanel = new RunPanel();
    //content = runPanel.renderPanel();
    //$('#div-component-2').html(content);

    var report = new TestReport();
    report.getInfo();
    content = report.renderPanel();
    $('#div-component-3').html(content);

    //$('#spn-report-badge').text('123');

    //$("#div-component-2").text('');
    //$("#div-component-2").load("/project/reports/html/TESTS-Sf02_AddProduct.html .container .panel-default");

    console.log($('#lnk-abc').attr('data-path'));
});

$("#lnk-load-config").on("click", function() {
    //console.log('load config');
    $('#file-config').click();
    //$('#frm-load-config').submit();
});

$("#file-config").on("change", function() {
    $('#frm-load-config').submit();
});

$('#btn_run').on('click', function() {
    $('#btn_run').attr('disabled', 'disabled');
    $('#btn_run').text('Running...');

    options = $('#txt_options').val();

    var report = new TestReport();
    report.clear();

    timer = setInterval( function() {
        cout = new ConsoleOutput();
        cout.getInfo()
        cout.render();
    }, 1000);

    $.ajax({
        type: 'get',
        url: '/api/run/start',
        data: {
            "options": options
        },
        success: function (data) {
            console.log('run tests success');

            $('#btn_run').text('Run Cylon');
            $('#btn_run').removeAttr('disabled');

            report.getInfo();
            report.renderHead();
            report.renderBody();

            clearInterval(timer);
        }
    });
});

// $('#btn_run').on('click', function() {
//     $('#pnl_reports').text('Waiting...');
//
//     $('#btn_run').attr('disabled', 'disabled');
//     $('#btn_run').text('Running...');
//
//     options = $('#txt_options').val();
//
//     //var interval = 1000;
//     //var timer = setTimeout(doAjax, interval);
//
//     /// start run ///
//     request = $.ajax({
//         url: "/api/run/start",
//         type: "get",
//         data: {
//             "options": options
//         }
//     })
//     .done( function(response, textStatus, jqXHR) {
//         $('#btn_run').text('Run Cylon');
//         $('#btn_run').removeAttr('disabled');
//
//         //clearTimeout(timer);
//         //generateReports();
//         //displayReports();
//     })
//     .fail(function (jqXHR, textStatus, errorThrown) {
//         console.error("The following error occurred: " + textStatus, errorThrown);
//     });
// });


function ConsoleOutput() {
    this.info = undefined;

    this.getInfo = function() {
        var response = undefined;

        $.ajax({
            type: 'get',
            url: '/api/run/console',
            dataType: 'text',
            async: false,
            success: function (data) {
                console.log(data);
                response = data;
            }
        });

        this.info = response;
    }

    this.render = function() {
        $('#hidden').html(this.info.toString());
    }

    // this.start = function() {
    //     this.timer = setInterval(this.render, this.interval);
    // }
    //
    // this.stop = function() {
    //     clearInterval(this.timer);
    // }
}


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
        url: "/api/run/console",
        type: "get",
        dataType: "text"
    })
    .done( function (response, textStatus, jqXHR) {
        content = response.toString();
        //content = content.replace(/(?:\r\n|\r|\n)/g, '<br/>');
        //content = content.replace(/(?:\s)/g, '&nbsp;&nbsp;');
        //content = content;
        $('#hidden').html(content);
    });
};

//tm.start();
