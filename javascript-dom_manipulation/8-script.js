document.addEventListener('DOMContentLoaded', () => {
  const translate = document.querySelector('#hello');
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      translate.textContent = data.hello;
    })
    .catch(error => console.error(error));
});
