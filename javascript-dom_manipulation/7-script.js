const list = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(film => {
      const newElement = document.createElement('li');
      newElement.textContent = film.title;
      list.append(newElement);
    });
  })
  .catch(error => console.error(error));
