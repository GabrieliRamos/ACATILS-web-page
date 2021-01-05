var form = document.querySelector('#contact_form')
var campos = form.querySelectorAll('div > *')

form.addEventListener('submit', function(e) {
    // alerta o valor do campo
    console.log(campos)
    console.log(`${campos[0].value} - ${campos[1].value} - ${campos[2].value} - ${campos[3].value}`)
    
    // impede o envio do form
    e.preventDefault()
});