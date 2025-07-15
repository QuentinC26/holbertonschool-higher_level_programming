const the_text = document.getElementById("update_header");
const list = document.querySelector("header");

add_item.addEventListener("click", new_text);

function new_text() { 
    const new_text = the_text.classList;
    new_text.remove("Update the header");
    new_text.add("New Header!!!");
};
