function addToCart() {
    let button = document.getElementById("btn-add-cart");
    const prod_id = parseInt(button.value);

    // csrfmiddlewaretoken

    const url = '/cart/add';
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.log(csrf);

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
            let cardCount = document.getElementById('cart-count');
            const count = parseInt(cardCount.textContent);
            console.log((count + 1).toString())
//            cardCount.textContent = (count + 1).toString();
        }
    });
}