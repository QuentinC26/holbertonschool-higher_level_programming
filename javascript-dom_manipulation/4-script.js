document.addEventListener("click", add_item, false)

function add_item() {
    const_list = document.querySelector('.my_list');
    const tag = document.createElement("li");
    const text = document.createTextNode("Item");
    tag.appendChild(text);
    const addItemElement = myList.appendChild(tag)
}
