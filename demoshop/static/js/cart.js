function addToCart() {
    let button = document.getElementById("btn-add-cart");
    const prod_id = parseInt(button.value);

    // csrfmiddlewaretoken

    const url = '/cart/add';
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const json = JSON.stringify(
        {
            product_id: prod_id,
        }
    );

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf,
            'Content-Type': "application/json"
        },
        body: json
    }).then(function (response){
        if(response.ok){
            let cartCount = document.getElementById('cart-count');
            const count = parseInt(cartCount.textContent);

//            cartCount.textContent = (count + 1).toString();
        }
    });
}