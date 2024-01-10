$.get('https://swapi.co/api/people/5/?format=json', function (props) {
  $('DIV#character').text(props.name);
});
