from django.urls import path
from . import views
from store.controller import cart, checkout, order

urlpatterns = [
    path("single/<str:movie_name>", views.single, name="single"),
    path("add-to-cart", cart.addtocart, name="addtocart"),
    path("tickets", cart.showtickets, name="tickets"),
    path("delete-cart-item", cart.deletecartitem, name="deletecartitem"),
    path("checkout", checkout.index, name="checkout"),
    path("placeorder", checkout.placeorder, name="placeorder"),
    path("proceed-to-pay", checkout.proceedtopay1, name="proceedtopay1"),
    path("my-orders", order.index, name="myorders")
]