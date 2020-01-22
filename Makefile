all:
	venv/bin/python3 resume.py
	pdflatex Resume.tex

clean:
	rm Resume.tex
	rm Resume.aux
	rm Resume.log
	rm Resume.pdf

