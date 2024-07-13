//Funciones JavaScript para el carrito de compras
var cart = JSON.parse(localStorage.getItem('cart')) || [];

function addToCart(item, price) {
    cart.push({name: item, price: Number(price)});
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCart();
    alert(item + ' fue añadido a tu carrito!');
}


function removeFromCart(item) {
    var index = cart.findIndex(cartItem => cartItem.name === item);
    if (index > -1) {
        cart.splice(index, 1);
    }
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCart();
}

function displayCart() {
    var cartItemsDiv = document.getElementById('cartItems');
    cartItemsDiv.innerHTML = '';
    var cart = JSON.parse(localStorage.getItem('cart')) || [];
    for (var i = 0; i < cart.length; i++) {
        cartItemsDiv.innerHTML += '<div class="dropdown-item">' + cart[i].name + ' - ' + cart[i].price + '<button onclick="removeFromCart(\'' + cart[i].name + '\')">Eliminar</button></div>';
    }
    displayCartDetails();
}

function displayCartDetails() {
    var cartDetails = document.getElementById('cartDetails');
    var cartTotal = document.getElementById('cartTotal');
    cartDetails.innerHTML = '';
    cartTotal.innerHTML = '';
    var total = 0;
    for (var i = 0; i < cart.length; i++) {
        total += cart[i].price;
        cartDetails.innerHTML += '<tr><td>' + cart[i].name + '</td><td>' + cart[i].price + '</td><td><button onclick="removeFromCart(\'' + cart[i].name + '\')" style="background-color: #faae50; color: white;">X</button></td></tr>';
    }
    cartTotal.innerHTML = '<h4>Total: $' + total + '</h4>';
}

function clearCart() {
    cart = [];
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCart();
}




//Validaciones con jQuery
//VALIDAR FORMULARIO DE CONTACTO
$(document).ready(function(){
    $("#validarFormulario").submit(function(event){
        // evitar que el formulario se envíe automáticamente
        event.preventDefault();
        
        // validaciones
        var edad = $("#edad").val();
        var nombre = $("#nombre").val();
        var apellido = $("#apellido").val();

        if(edad < 18){
            alert("Debes ser mayor de edad para enviar comentarios.");
            return;
        }
        if(edad > 99){
            alert("Edad inválida.");
            return;
        }
        // nombre, apellidos: largo entre 3 y 20 caracteres
        if(nombre.length < 3 || nombre.length > 20 ||
            apellido.length < 3 || apellido.length > 20){
            alert("El Nombre y los Apellidos deben tener entre 3 y 20 caracteres.");
            return;
        }
        else{
            // validaciones aceptadas
            alert("¡Mensaje recibido con exito!");
            // limpiar el formulario
            $("#validarFormulario")[0].reset();
        }       
    });
});


//DESCUENTO DE PRODUCTOS
var products = document.getElementsByClassName('product');

for (var i = 0; i < products.length; i++) {
    var discount = products[i].getAttribute('data-discount');
    if (discount) {
        var discountLabel = products[i].getElementsByClassName('discount-label')[0];
        discountLabel.style.display = 'block';
        discountLabel.textContent = discount + '% ';
    }
}
//MANEJAR EL COMPORTAMIENTO DEL SUBMENU
document.addEventListener('DOMContentLoaded', function() {
    // Handle click on submenus to prevent default behavior and propagation
    document.querySelectorAll('.dropdown-submenu a.dropdown-toggle').forEach(function(element) {
        element.addEventListener('click', function(e) {
            if (!this.nextElementSibling.classList.contains('show')) {
                this.closest('.dropdown-menu').querySelectorAll('.show').forEach(function(subMenu) {
                    subMenu.classList.remove('show');
                });
            }
            var subMenu = this.nextElementSibling;
            subMenu.classList.toggle('show');
            return false;
        });
    });
    
    // Prevent closing the menu when clicking inside the submenu
    document.querySelectorAll('.dropdown-menu').forEach(function(element) {
        element.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    });
});