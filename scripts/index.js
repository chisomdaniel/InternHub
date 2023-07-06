$('document').ready(function () {
    const urlpath = 'http://' + window.location.hostname;
});

let internship = {};
$('.')
$('button').click(function () {
    $.ajax({
        url: urlpath + ':5001/api/version1/get_jobs/',
        type: 'POST',
        data: JSON.stringify({
            'internship': Object.keys(internship)
        }),
        contentType: 'application/json',
        dataType: 'json',
        success:
    })
})