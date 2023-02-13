$(document).ready(function () {
    $('.addToWatchbtn').click(function (e) { 
        e.preventDefault();
        var film_id = $('.film_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/store/add-to-cart",
            data: {
                'film_id' : film_id,
                csrfmiddlewaretoken: token 
            },
            success: function (response) {
                console.log(response)
                alertify.success(response.status)
            }
        });
        
    });
    
    $('.delete-cart-item').click(function (e) { 
        e.preventDefault();
        var film_id = $(this).closest('.product_data').find('.film_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "delete-cart-item",
            data: {
                'film_id' : film_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response)
                $('.cartdata').load(location.href + " .cartdata");
            }
        });
    });
});