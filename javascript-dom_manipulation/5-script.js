document.getElementById('update_header').addEventListener('click', () => {
  const header = document.querySelector('header');
  header.textContent = 'New Header !!!';
});

// You can also do that if the project is more complex:
/*
const header = document.querySelector('header');
const update_header = document.querySelector('#update_header');
update_header.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
*/
