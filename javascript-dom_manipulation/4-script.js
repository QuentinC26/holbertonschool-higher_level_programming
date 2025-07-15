document.addEventListener("click", add_item, false)

function add_item() {
    const header = document.getElementById("add_list");
    const list = document.querySelector('my_list');
    const tag = document.createElement("li");
    const text = document.createTextNode("Item");
    tag.appendChild(text);
    const addItemElement = add_list.appendChild(tag);
}
