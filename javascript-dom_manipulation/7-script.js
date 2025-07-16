async function getMovies() {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`The request as failed: ${response.status}`);
    }

    const json = await response.json();
    const resultsMovieName = json.films;
    const movies = []
    length_movies = films.length
    length_list_movies = movies.length
    for (index = 0; index < length_movies; index++) {
        if (key = "title") {
            movies.append(value);
        }
    }
    for (index_two = 0; index_two < length_list_movies; index_two++) {
        const tag = document.createElement("li");
        const movie_name = document.createTextNode(index_two);
        document.getElementById("list_movies")
        tag.appendChild(movie_name);
        list_movies.appendChild(tag);
    }
  } 
  catch (error) {
    console.error(error.message);
  }
}
getMovies();
