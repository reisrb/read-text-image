
create_env:

	python3 -m venv .env

enter_env:

	source .env/bin/activate

install_packages:

	pip3 install -r requirements.txt

>Run server with html for upload from a image and return of text

run_server:

	python3 main.py

>Read text in local image

run_local:

	python3 local_img.py $(path)
	

>Run this command to correct space problem when installing easyocr lib

	export TMPDIR='/var/tmp'

