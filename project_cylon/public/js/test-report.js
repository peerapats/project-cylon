
function TestReport()
{
    this.info = undefined;

    this.getInfo = function() {
        var response = undefined;

        $.ajax({
            type: 'get',
            url: '/api/report/info',
            dataType: 'json',
            async: false,
            success: function (data) {
                response = data;
            }
        });

        this.info = response;
    }

    this.render = function() {
        return this.renderPanel();
    }

    this.renderPanel = function() {
        var table = this.renderTable();

        var panel = '\
            <div class="panel panel-default">\n\
              <div class="panel-heading"><strong>Test Reports:</strong></div>\n\
              <div class="panel-body">'+ table +'</div>\n\
            </div>\n\
        ';
        return panel;
    }

    this.renderTable = function() {
        var thead = this.renderHead();
        var tbody = this.renderBody();

        var table = '\
            <table class="table table-hover">\n\
              <thead>'+ thead +'</thead>\n\
              <tbody>'+ tbody +'</tbody>\n\
            </table>\n\
        ';
        return table;
    }

    this.renderHead = function() {
        var thead = '\
            <tr>\n\
              <th>Feature</th>\n\
              <th class="text-center">Passed</th>\n\
              <th class="text-center">Failed</th>\n\
              <th class="text-center">Total</th>\n\
              <th class="text-center">Status</th>\n\
              <th class="text-center">Duration</th>\n\
            </tr>\n\
        ';
        return thead;
    }

    this.renderBody = function() {
        var tbody = '';

        for (i = 0; i < this.info.files.length; i++) {
            item = this.info.files[i];
            tbody += this.renderRow(item.filename, item.passed, item.failed, item.total, item.status, item.duration);
        }
        return tbody;
    }

    this.renderRow = function(feature, passed, failed, total, status, duration) {
        var colors = {
            "passed":  "text-success",
            "failed":  "text-danger",
            "skipped": "text-primary"
        };

        path = this.info.path;

        feature  = '<a href="'+ path +'/'+ feature +'" target="_blank">'+ feature +'</a>';
        passed   = '<div>'+ passed +'</div>';
        failed   = '<div>'+ failed +'</div>';
        total    = '<div>'+ total +'</div>';
        status   = '<div class="'+ colors[status] +'">'+ status +'</div>';
        duration = '<div>'+ duration +'</div>';

        var content = '\
            <tr>\n\
              <td>'+ feature +'</td>\n\
              <td class="text-center">'+ passed +'</td>\n\
              <td class="text-center">'+ failed +'</td>\n\
              <td class="text-center">'+ total +'</td>\n\
              <td class="text-center">'+ status +'</td>\n\
              <td class="text-center">'+ duration +'</td>\n\
            </tr>\n\
        ';
        return content;
    }
}
