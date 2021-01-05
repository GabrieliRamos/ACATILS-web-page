const currentPage = location.pathname
const menuItems = document.querySelectorAll("ul li a")

for (item of menuItems) {
    if (currentPage.includes(item.getAttribute("href"))) {
        item.classList.add("active")
    }
}

/* menu toggle */
let show = true;

const menuSection = document.querySelector(".menu-section")
const menuToggle = menuSection.querySelector(".menu-toggle")

menuToggle.addEventListener('click', () => {
    document.body.style.overflow = show ? "hidden" : "initial"
    menuSection.classList.toggle('on', show)
    show = !show
})

menuToggle.addEventListener('mouseover', () => {
    let div = menuToggle.querySelectorAll("div")

    for (let i = 0; i < div.length; i++) {
        div[i].style.backgroundColor = "#31a24c"
    }
})

menuToggle.addEventListener('mouseout', () => {
    let div = menuToggle.querySelectorAll("div")

    for (let i = 0; i < div.length; i++) {
        div[i].style.backgroundColor = "#555"
    }
})