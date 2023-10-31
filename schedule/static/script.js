// document.addEventListener('DOMContentLoaded', function() {
//     const titleLeft = document.querySelector('.title-left');
//     const inputFields = document.getElementById('fields');

//     titleLeft.addEventListener('click', function() {
//         if (inputFields.style.display === 'none' || inputFields.style.display === '') {
//             inputFields.style.display = 'grid';
//         } else {
//             inputFields.style.display = 'none';
//         }
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    const mediaQuery = window.matchMedia("(max-width: 1562px)");
    const titleLeft = document.querySelector('.title-left');
    const inputFields = document.getElementById('fields');

    const handleMediaQueryChange = (event) => {
        if (event.matches) {
            titleLeft.addEventListener('click', toggleInputFields);
        } else {
            titleLeft.removeEventListener('click', toggleInputFields);
            inputFields.style.display = 'grid'; // Garante que o campo seja exibido para telas maiores que 1560px
        }
    };

    const toggleInputFields = () => {
        if (inputFields.style.display === 'none' || inputFields.style.display === '') {
            inputFields.style.display = 'grid';
        } else {
            inputFields.style.display = 'none';
        }
    };

    mediaQuery.addEventListener('change', handleMediaQueryChange);
    handleMediaQueryChange(mediaQuery); // Verifica o estado da media query ao carregar a página
});