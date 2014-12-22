function ProjectBar()
{
    this.config = undefined;

    this.getInfo = function() {
        var response = undefined;

        $.ajax({
            type: 'get',
            url: '/api/project/get_config',
            dataType: 'json',
            async: false,
            success: function (data) {
                response = data;
            }
        });

        this.config = response;
    }

    this.render = function() {

    }

    this.renderProjectMenu = function() {

    }
}
