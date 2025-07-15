const the_text = document.getElementById("update_header");

the_text.addEventListener("click", new_text);

function new_text() { 
    document.getElementById("update_header").innerHTML = "New Header!!!";
};
