function ShowIframe() {
    const iframe = document.querySelector('#iframe-translate')
    const img = document.querySelector('#translate-icon')

    if (iframe.style.display != 'flex') {
        iframe.style.display = 'flex'
        img.src = '/static/img/close-icon.png'
        img.style.filter = 'invert(100%)'
    } else {
        iframe.style.display = 'none'
        img.src = '/static/img/libras-icon.png'
        img.style.filter = 'invert(0%)'
    }
}