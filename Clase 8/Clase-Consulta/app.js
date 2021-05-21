document.addEventListener('DOMContentLoaded', () => {
    const calculadora = document.querySelector(".calculadora")
    const display = document.querySelector(".calculadora__display")
    const botones = calculadora.querySelector(".calculadora__botones")


    botones.addEventListener('click', e => {
        if (e.target.matches('button')) {
            const tecla = e.target;
            const accion = tecla.dataset.accion;
            if(!accion) {
                console.log("Esto es un numero")
            }
            if (accion == 'sumar' || accion == 'restar' || accion == 'multiplicar' || accion == 'dividir') {
                console.log("operacion");
            }
            if (accion == 'decimal') {
                console.log('decimal');
            }
            if (accion == 'borrar') {
                console.log('borrar');
            }
            if (accion == 'calculo') {
                console.log('calculo');
            }
        }
    });
});