document.getElementById('add_item').addEventListener('click', function () {
  const new_item = document.createElement('li');
  new_item.textContent = 'Item';
  document.querySelector('.my_list').appendChild(new_item);
});
