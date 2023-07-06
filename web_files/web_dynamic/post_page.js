$(function() {
    $("#submit-button").click(function() {
        const myData = {};

        var data = $("#post-form").serializeArray();
        $.each(data, function(i, field) {
            $("#output").append(field.name + ":"
                            + field.value + " ");
            myData[field.name] = field.value;
        });
        console.log(myData)

        url1 = 'http://localhost:5000/api/version1/jobs';
        console.log("Started posting")
        $.ajax({
            url: url1,
            type: "POST",
            data: JSON.stringify(myData),
            contentType: "application/json",
            success: function (data) {
                $.each(data, function(index, value) {
                    $(".post-info").append("<em>Posted Successfully</em>")
                    console.log("Done")
                });
            }
        });
    });
});