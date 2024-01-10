$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (enter) {
      if (enter.keycode === 13) {
        translate();
      }
    });
  });
});

function translate () {
  const link = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(link + $.param({ lang: $('INPUT#language_code').val() }), function (props) {
    $('DIV#hello').html(props.hello);
  });
}
