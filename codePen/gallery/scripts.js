var one = document.getElementById('one');
var two = document.getElementById('two');
var three = document.getElementById('three');
var four = document.getElementById('four');


// Function to enlarge image
function enlargeImg(img) {
    // Set image size to 1.5 times original
    img.style.transform = "scale(1.2)";
    // Animation effect
    img.style.transition = "transform 0.25s ease";
    img.style.scale = "2";
    img.style.right = "10px";
}
// Function to reset image size
function resetImg(img) {
    // Set image size to original
    img.style.position = "relative";
    img.style.scale = "1";
    img.style.transform = "scale(1)";
    img.style.transition = "transform 0.25s ease";
}