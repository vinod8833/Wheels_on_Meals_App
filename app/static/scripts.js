function scrollLeft(containerId) {
    const container = document.getElementById(containerId);
    container.scrollBy({
        left: -300,
        behavior: 'smooth' 
    });
}

function scrollRight(containerId) {
    const container = document.getElementById(containerId);
    container.scrollBy({
        left: 300,
        behavior: 'smooth' 
    });
}

document.querySelector('.scroll-button.left').addEventListener('click', function() {
    scrollLeft('restaurant-list');
});

document.querySelector('.scroll-button.right').addEventListener('click', function() {
    scrollRight('restaurant-list');
});




