$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (props) {
    $('DIV#hello').text(props.hello);
  });
});
