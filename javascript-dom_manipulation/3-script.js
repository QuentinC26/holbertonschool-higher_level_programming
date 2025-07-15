const header = document.getElementById("toggle_header");
if (header.classList.contains("red") == true) {
    header.classList.remove("red");
    header.classList.add("green");
} else {
    header.classList.add("green");
}
