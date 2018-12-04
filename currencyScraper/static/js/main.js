/*let currencyBtn = document.querySelector('#currency-btn');
let cryptocurrencyBtn = document.querySelector('#cryptocurrency-btn');
let forexBtn = document.querySelector('#forex-btn');

let hiddenContent = document.getElementById('collapse-element');

let currencyLinks = ['mymoney.pl', 'cinkciarz.pl', 'bankier.pl'];
let cryptocurrencyLinks = ['cos1', 'co2', 'cos3'];
let forexLinks = ['cos4', 'cos5', 'cos6'];

// Event listeners for buttons
currencyBtn.addEventListener('click', function() { 
    showLinks(...currencyLinks);
});

cryptocurrencyBtn.addEventListener('click', function() {
    showLinks(...cryptocurrencyLinks);
});

forexBtn.addEventListener('click', function() {
    showLinks(...forexLinks);
});


function showLinks(link1, link2, link3) {
    let template = '';

    template += `
        <div class="content row justify-content-md-center">
            <div class="col-sm-3">
                <a href="">${link1}</a>
             </div>
            <div class="col-sm-3">
                <a href="">${link2}</a>
             </div>
            <div class="col-sm-3">
                <a href="">${link3}</a>
            </div>
        </div>
    `;

    hiddenContent.style.display = 'block';
    hiddenContent.innerHTML = template;
}*/
