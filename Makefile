dokerRun:
	docker run -p 8080:8080 proxy
	docker run -it scaner bash

dockerBuild:
	docker build -t proxy .
	docker image build -t scaner -f scaner.Dockerfile  .