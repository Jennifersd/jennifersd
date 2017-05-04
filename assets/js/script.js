// Menu 

(function() {
    var burger = document.querySelector(".burger-container"),
        header = document.querySelector(".header-container");

    burger.onclick = function() {
        header.classList.toggle("menu-opened");
    };
})();
