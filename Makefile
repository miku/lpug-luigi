slides.pdf: slides.md
	pandoc -t beamer slides.md -V theme:Singapore -colortheme:dove -o slides.pdf

plays.ldj:
	python makesample.py > plays.ldj

clean:
	rm -f slides.pdf plays.ldj
