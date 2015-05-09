{% block content %}
	var amaduoRoutes = function(){
	{% for model, primary_key in models.items %}
		this.resource('{{ model }}', { path: '/{{ model }}/:{{ model }}_{{ primary_key | safe }}' });
	{% endfor %}
	}
{% endblock %}