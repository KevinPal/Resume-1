all:
	python resume.py
	pdflatex Resume.tex

clean:
	rm Resume.tex
	rm Resume.aux
	rm Resume.log
	rm Resume.pdf

