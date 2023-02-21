build:
	docker build . -t flan-t5:1.0.0
dev:
	docker run -p 8080:8080 --rm -it flan-t5:1.0.0
