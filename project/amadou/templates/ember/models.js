{% block content %}

	<!--  Build Ember Models -->
	{% for model, fields in models.items %}
		App.{{ model }} = DS.Model.extend({
		{% for field_name, field_type in fields.items %}
			{{ field_name }} : {{ field_type | safe }},
		{% endfor %}
		});
	{% endfor %}
	
	
{% endblock %}