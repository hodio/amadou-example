{% block content %}
	<!--  Build Ember Resource Rotues -->
	{% for app, models in apps.items %}
		{% for model in models %}
			
			// Plural
			App.{{ model | title }}sRoute = Ember.Route.extend({
				model: function() {
					return this.store.find('{{ model }}');
				},
				setupController: function(controller, model) {
					var metadata = this.store.metadataFor('{{ model }}');
					controller.set('model', model);
				},
				renderTemplate: function() {
				    this.render('{{ app }}/{{ model }}s')         
				}
			});
			
			// Singular
			App.{{ model | title }}Route = Ember.Route.extend({
				model: function() {
					return this.store.find('{{ model }}');
				},
				setupController: function(controller, model) {
					var metadata = this.store.metadataFor('{{ model }}');
					controller.set('model', model);
				},
				renderTemplate: function() {
				    this.render('{{ app }}/{{ model }}')         
				}
			});
		{% endfor %}
	{% endfor %}
{% endblock %}