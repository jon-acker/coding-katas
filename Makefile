project-clean: ## clean all project specific containers and images (add "all" to remove images)
	docker kill   $$(docker     ps -qa -f "label=project=${COMPOSE_PROJECT}") 2>/dev/null || true
	docker rm     $$(docker     ps -qa -f "label=project=${COMPOSE_PROJECT}") 2>/dev/null || true
	[ "x$(RUN_ARGS)" == 'xall' ] && (docker rmi -f $$(docker images -qa -f "label=project=${COMPOSE_PROJECT}")) 2>/dev/null || true
	[ "x$(RUN_ARGS)" == 'xall' ] && (docker rmi -f $$(docker images -qa -f "dangling=true")) 2>/dev/null || true
	yes | docker network prune 2>/dev/null || true
	yes | docker volume prune 2>/dev/null || true
	yes | docker system prune 2>/dev/null || true


make test-js:
	docker-compose exec node node_modules/.bin/mocha js/spec/
