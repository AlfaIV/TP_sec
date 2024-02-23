dokerRun:
	docker run -p 8080:8080 proxy
	docker run -it scaner bash

dockerBuild:
	docker build -t proxy .

dockerPostgres:
	docker image build -t postgres -f db.Dockerfile ./db/
	docker run -p 5432:5432 postgres

dockerProxy:
	docker image build -t proxy ./proxy_src/
	docker run -p 5432:5432 proxy

dockerScaner:
	docker build -t proxy .
	docker image build -t scaner -f scaner.Dockerfile  .