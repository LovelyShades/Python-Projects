// script.js

document.addEventListener("DOMContentLoaded", function () {
    const menuToggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector("nav ul");

    menuToggle.addEventListener("click", function () {
        nav.classList.toggle("showing");
    });

    const links = document.querySelectorAll('a[href^="#"]');

    for (const link of links) {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            const targetId = this.getAttribute("href");
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: "smooth"
                });
            }
        });
    }
});
