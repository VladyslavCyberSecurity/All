document.addEventListener('DOMContentLoaded', function() { //product.html поле коментариев
  var elems = document.querySelectorAll('.autocomplete');
  var instances = M.Autocomplete.init(elems, options);
});
// Or with jQuery
$(document).ready(function(){
  $('input.autocomplete').autocomplete({
    data: {
      "Apple": null,
      "Microsoft": null,
      "Google": 'https://placehold.it/250x250'
    },
  });
});

var slider = document.getElementById('test-slider'); // не работает
noUiSlider.create(slider, {
 start: [20, 80],
 connect: true,
 step: 1,
 orientation: 'horizontal', // 'horizontal' or 'vertical'
 range: {
   'min': 0,
   'max': 100
 },
 format: wNumb({
   decimals: 0
 })
});
