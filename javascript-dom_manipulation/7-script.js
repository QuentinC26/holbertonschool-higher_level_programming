async function getMovies() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`The request as failed: ${response.status}`);
    }

    const json = await response.json();
    const resultsMovieName = json.results;
    movies = []
    for (key, value in resultsMovieName) {
        if (key = "title") {
            movies.append(value);
        }
    }
    for (index in movies){
        document.getElementById("list_movies").innerText = index;
        index = index + 1
    }
  } 
  catch (error) {
    console.error(error.message);
  }
}
getMovies();
