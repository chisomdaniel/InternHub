$(document).ready(function() {
    $.ajax({
        url: 'http://localhost:5000/api/version1/jobs',
        method: 'GET',
        success: function(response) {
            response.forEach(function(data) {
                let elem = $('<article>').text(data);
                $('.alljob').append(elem);
            });
        },
        });
    });