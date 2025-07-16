async function getHello() {
  const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`The request as failed: ${response.status}`);
    }

    const json = await response.json();
    Hello_in_French = document.getElementById("hello");
    Hello_in_French.innerText = json.hello;
  }
  catch (error) {
    console.error(error.message);
  }
}
getHello();
