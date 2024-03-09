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
    }).then((response) => response.json())
      .then((data) => {
        let cartCount = document.getElementById('cart-count');
        count = data.cart_count.toString();
        cartCount.textContent = count;
    });
}