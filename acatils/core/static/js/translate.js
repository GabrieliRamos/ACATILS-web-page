function ShowIframe() {
    const iframe = document.querySelector('#iframe-translate')
    const img = document.querySelector('#translate-icon')

    if (iframe.style.display != 'flex') {
        iframe.style.display = 'flex'
        img.style.filter = 'invert(100%)'
        img.src = '/static/img/close-icon.png'
    } else {
        iframe.style.display = 'none'
        img.style.filter = 'invert(0%)'
        img.src = '/static/img/libras-icon.png'
    }
}