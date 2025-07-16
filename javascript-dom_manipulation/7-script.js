async function getMovies() {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`The request as failed: ${response.status}`);
    }

    const json = await response.json();
    const moviesName = json.results;
    for (let index in moviesName) {
        add_title = moviesName[index].title;
        moviesName.push(add_title);
        const tag = document.createElement("li");
        tag.appendChild(moviesName);
        const list_movies = document.getElementById("list_movies");
        list_movies.appendChild(tag);
    }
  }
  catch (error) {
    console.error(error.message);
  }
}
getMovies();
