const btnAddProduct = document.getElementById('btn-add-product');
const errorBlock = document.getElementById('error-block');
const host = window.location.host;
const url = 'http://' + host;
const urlAddProduct = url + '/api/v1/products/create/';
const formAddProduct = document.getElementById('form-add-product');


btnAddProduct.onpointerup = AddProduct;


async function AddProduct (event) {
    errorBlock.innerHTML = '';
    let response = await fetch(urlAddProduct, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(parseForm())
        });
    error_elem = document.createElement('h4');
    error_elem.textContent = 'Ошибка. '
    if (response.ok) {
        window.location.href = url;
    }
    else {
        let result = await response.json();
        name_result = result.name;
        price_result = result.price;
        if (name_result !== null) {
            error_elem.textContent += name_result
        }
        if (price_result !== null) {
            error_elem.textContent += price_result
        }
        if (name_result === null & price_result === null) {
            error_elem.textContent += 'Отсутствует соединение с сервером'
        };
        errorBlock.appendChild(error_elem);
        errorBlock.style.display = 'block';
    };
};

function parseForm () {
    return {
        'name': document.getElementById('id_name').value,
        'description': document.getElementById('id_description').value,
        'price': document.getElementById('id_price').value,
        'csrfmiddlewaretoken': document.getElementsByName('csrfmiddlewaretoken')[0].value
    };
};