$(document).ready(function () {
     $('.payWithRazorpay').click(function (e) { 
        e.preventDefault();

        var names = $("[name='ticketOwner'").val();
        var token = $("[name='csrfmiddlewaretoken']").val();
        if (names==""){
            swal({
                title: "Error",
                text: "Ticket Owner's name required!",
                icon: "error",
                button: "Edit!",
              });
            return false;
        }
        else{
            $.ajax({
                method: "GET",
                url: "/store/proceed-to-pay",
                success: function (response) {
                    // console.log(response)

                    var options = {
                        "key": "rzp_test_DFk7PJD4cgzXVV", // Enter the Key ID generated from the Dashboard
                        "amount": response.usdp * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "USD",
                        "name": "Kifule Cinema",
                        "description": "Thank you for supporting kifule Cinema",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (responseb){
                            alert(responseb.razorpay_payment_id);
                            data = {
                                "names" : names,
                                "payment_mode": "paid by RazorPay",
                                "payment_id": responseb.razorpay_payment_id,
                                csrfmiddlewaretoken: token
                            }
                            $.ajax({
                                method: "POST",
                                url: "placeorder",
                                data: data,
                                success: function (responsec) {
                                    swal("Congs!", responsec.status, "success").then((value) => {
                                      window.location.href = '/store/my-orders'
                                      });
                                }
                            });
                        },
                        "prefill": {
                            "name": names,
                            "email": "kunoomaking@gmail.com",
                            "contact": "256703750531"
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            });

            
        }


     });
});