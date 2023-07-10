$(function() {
    $("#post-form").submit(function(event) {
        event.preventDefault();
        const myData = {
            title: $('#title').val(),
            company: $('#company').val(),
            company_website: $('#company_website').val(),
            company_email: $('#company_email').val(),
            phone_number: $('#phone_number').val(),
            city: $('#city').val(),
            state: $('#state').val(),
            country: $('#country').val(),
            position_type: $('#position_type').val(),
            description: $('#description').val(),
            responsibility: $('#responsibility').val(),
            requirement: $('#requirement').val(),
            skill: $('#skill').val(),
            benefit: $('#benefit').val(),
            apply: $('#apply').val(),
            expire: $('#expire').val(),
            note: $('#note').val(),
            closing: $('#closing').val()
        };

        /*
        var data = $("#post-form").serializeArray();
        $.each(data, function(i, field) {
            $("#output").append(field.name + ":"
                            + field.value + " ");
            myData[field.name] = field.value;
        });
        console.log(myData)
        */

        console.log(myData)
        url1 = 'http://localhost:5000/api/version1/jobs';
        console.log("Started posting")
        $.ajax({
            url: url1,
            type: "POST",
            data: JSON.stringify(myData),
            contentType: "application/json",
            success: function (response) {
                $(".post-info").append("<em>Posted Successfully</em>")
                console.log("Done:", response);
                alert("Posted successfully");

                $('#title').val(''),
                $('#company').val(''),
                $('#company_website').val(''),
                $('#company_email').val(''),
                $('#phone_number').val(''),
                $('#city').val(''),
                $('#state').val(''),
                $('#country').val(''),
                $('#position_type').val(''),
                $('#description').val(''),
                $('#responsibility').val(''),
                $('#requirement').val(''),
                $('#skill').val(''),
                $('#benefit').val(''),
                $('#apply').val(''),
                $('#expire').val(''),
                $('#note').val(''),
                $('#closing').val('')
            }
        });
    });
});