async function getCharacter() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`The request as failed: ${response.status}`);
    }

    const json = await response.json();
    const characterName = json.name;
    const character = document.getElementById("character")
    character.innerText = characterName;
    document.getElementById("").innerHTML = json.name;
  } catch (error) {
    console.error(error.message);
  }
}
