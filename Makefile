dokerRun:
	docker run -p 8080:8080 proxy

dockerBuild:
	docker build -t proxy .