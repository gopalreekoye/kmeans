#reekoye gopal
#rkygop001

#k-means clustering assignment
#makefile
#20/05/2021


install: venv
	. venv/bin/activate; pip3 install -Ur requirements.txt

venv:
	test -d venv || python3 -m venv venv

clean:
	rm -rf venv
	find -iname "*.pyc" -delete
