const add_item = document.getElementById("add_item");
const list = document.querySelector(".my_list");

add_item.addEventListener("click", new_item);

function new_item() { 
    const tag = document.createElement("li");
    const text = document.createTextNode("Item");
    tag.appendChild(text);
    list.appendChild(tag);
};
