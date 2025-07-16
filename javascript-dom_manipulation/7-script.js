async function getMovies() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`The request as failed: ${response.status}`);
    }

    const json = await response.json();
    const MovieName = json.title;
    document.getElementById("list_movies").innerText = MovieName;
  } 
  catch (error) {
    console.error(error.message);
  }
}
getMovies();
