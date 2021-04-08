import PyPDF2
import sys
inputs = sys.argv[1:]
def pdf_combiner(*args):
    merger = PyPDF2.PdfFileMerger()
    for pdf in args:
        print(pdf)
        merger.append(pdf)
    merger.write("super.pdf")
        
pdf_combiner('dummy.pdf','twopage.pdf','tilted.pdf')