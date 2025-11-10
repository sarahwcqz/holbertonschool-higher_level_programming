document.addEventListener('DOMContentLoaded', () => {
  const add = document.querySelector('#add_item');
  const remove = document.querySelector('#remove_item');
  const clear = document.querySelector('#clear_list');
  const list = document.querySelector('.my_list');

  add.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.append(newItem);
  });

  remove.addEventListener('click', () => {
    if (list.lastElementChild) {
      list.lastElementChild.remove();
    }
  });

  clear.addEventListener('click', () => {
    list.innerHTML = '';
  });
});
