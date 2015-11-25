.SILENT:

unit_test:
	python -m unittest test.py

pep8:
	pep8 parallelize/

test: pep8 unit_test
