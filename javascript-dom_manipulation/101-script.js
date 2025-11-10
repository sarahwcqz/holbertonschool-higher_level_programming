document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('#btn_translate');
  const trad = document.querySelector('#hello');
  const languages = document.querySelector('#language_code');

  button.addEventListener('click', () => {
    const selected = languages.value;
    fetch(`https://hellosalut.stefanbohacek.com/?lang=${selected}`)
      .then(response => response.json())
      .then(data => {
        trad.textContent = data.hello;
      })
      .catch(error => console.error(error));
  });
});
