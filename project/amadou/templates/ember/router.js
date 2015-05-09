{% block content %}
var amadouRouter = function(){
	{% for app, models in apps.items %}
		// {{ app | title }} 
		this.resource('{{ app }}',{ path : '/{{ app }}' },function(){
		
			{% for model in models %}
				// Plural
				this.resource('{{ model }}s');
				
				// Singular
				this.resource('{{ model }}');
			{% endfor %}
		
		});
	{% endfor %}
}	
{% endblock %}