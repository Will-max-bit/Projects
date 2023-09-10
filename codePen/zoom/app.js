var root = document.documentElement;

window.addEventListener('mouseup', function(e) {
    switch (e.button) {
        case 0: {
            root.style.setProperty('--scale-factor', 1)
        }
        case 1: {
            root.style.setProperty('--scale-factor', 20)
    // root.style.setProperty('--scale-factor', 1)
        }}})