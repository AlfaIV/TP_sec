dokerRun:
	docker run -p 8080:8080 proxy

dockerBuild:
	docker build -t proxy .

dockerPostgres:
	docker image build -t postgres -f db.Dockerfile ./db/
	docker run -p 5432:5432 postgres

dockerProxy:
	docker image build -t proxy ./proxy_src/
	docker run -p 5432:5432 proxy