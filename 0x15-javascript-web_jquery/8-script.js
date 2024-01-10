$.get('https://swapi.co/api/films/?format=json', function (props) {
  $('UL#list_movies').append(...props.results.map(movie => `<li>${movie.title}</li>`));
});
