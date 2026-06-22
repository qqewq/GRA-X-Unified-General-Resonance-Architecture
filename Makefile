install:
	pip install -e .

test:
	pytest tests/

lint:
	ruff check gra_core gra_math gra_semantic gra_subject gra_swarm gra_runtime gra_orchestra gra_memory gra_metrics gra_visualization api

format:
	black .

docs:
	mkdocs serve

docker-build:
	docker build -t gra-x -f docker/Dockerfile .

docker-run:
	docker compose -f docker/compose.yaml up
