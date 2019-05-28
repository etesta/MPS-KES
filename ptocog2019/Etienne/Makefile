all:PTCOG2019_Poster.pdf

PTCOG2019_Poster.pdf: PTCOG2019_Poster.tex
	pdflatex PTCOG2019_Poster.tex;						\
	while ( grep "Rerun to get" PTCOG2019_Poster.log >/dev/null ); do	\
		pdflatex PTCOG2019_Poster.tex;					\
	done

clean:
	rm -f *.aux *.dvi *.log *.out *.maf *.mt* *.toc *.backup *.maf *.mtc *.snm *.nav *.blg *.gz

nopdf:
	rm -f *.pdf
