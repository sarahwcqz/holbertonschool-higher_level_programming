const charName = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    charName.textContent = data.name;
  })
  .catch(error => console.error(error));
