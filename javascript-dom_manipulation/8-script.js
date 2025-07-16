async function getHello() {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`The request as failed: ${response.status}`);
    }

    const json = await response.json();
    const tag = document.createElement("head");
    Hello_in_French = document.getElementById("hello");
    Hello_in_French.appendChild(tag);
  }
  catch (error) {
    console.error(error.message);
  }
}
getHello();
