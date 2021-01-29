create_env:
	python3 -m venv .env

enter_env:
	source .env/bin/activate

install_packages:
	pip3 install -r requirements.txt

#run server with html for upload from a image and return of text
run_server:
	python3 main.py

#read text in local image
run_local:
	python3 local_img.py $(path)


	
build:
	docker build . -t ltmjobs:latest

run:
	docker run ltmjobs:latest $(mode) $(file)

create_env:
	python3 -m venv .env

all-test:
	python3 -m unittest discover test/

behavior-test:
	python3 -m unittest discover test/behavior/

unit-test:
	python3 -m unittest discover test/unit/
