$(function () {
    $.getJSON('http://localhost:5000/api/version1/jobs', function (data) {
        $.each(data, function (index, value) {
            const link = 'http://127.0.0.1:5001/internship/' + value.id;

            const article = $(`<article><h3>${value.title}</h3><b>${value.company}</b> <br>${value.description}<br><br>${value.city}, ${value.state}, ${value.country}<br><br><b>Position Type: ${value.position_type}</b></article>`);
            const section = $(`<section class="job"></section>`).append(article);
            const section_link = $(`<a href="${link}"></a>`).append(section);

            $(".alljob").append(section_link);

        });
    });
});