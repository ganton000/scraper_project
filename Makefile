.PHONY: start start_build stop unit_tests

UNIT_TESTS=pytest ./backend/tests

start:
	@docker-compose up -d

start_build:
	@docker-compose up --build -d

stop:
	@docker-compose down

unit_tests:
	docker-compose exec -T backend-tests $(UNIT_TESTS)

unit_tests_local:
	@$(UNIT_TESTS)

check_typing:
	@docker-compose exec -T backend-tests mypy ./backend

