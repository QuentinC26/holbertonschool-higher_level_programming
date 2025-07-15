const add_item = document.getElementById("add_item");

function new_item() {
    const list = document.querySelector('.my_list');
    const tag = document.createElement("li");
    const text = document.createTextNode("Item");
    tag.appendChild(text);
    list.appendChild(tag);
}
add_item.onclick = function() { 
    new_item();
 };
