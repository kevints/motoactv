check:
	python3 -m unittest tests/*.py

pex:
	pex.pex --source-dir=. --pex-name=motoactv --entry-point=motoactv:main

clean:
	rm motoactv.pex
