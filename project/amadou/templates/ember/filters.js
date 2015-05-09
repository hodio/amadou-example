Ember.Handlebars.helper('titleize', function(text) {
	var result = ''
	var list = text.toString().split('_');
	for (key in list){
		if (typeof list[key] == 'string'){
			result += list[key].charAt(0).toUpperCase() + list[key].slice(1) + ' ';
		}
	}
  return result;
});