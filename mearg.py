from PyPDF2 import PdfMerger

merger = PdfMerger()

pdf_files = ["meargpdf/1.pdf","meargpdf/2.pdf","meargpdf/3.pdf"] # enter the files name that you want to merge them together with the path of file 

for pdf_file in pdf_files:
    merger.append(pdf_file)


merger.write("meargpdf/123.pdf")# the the name of a mearge  file with the path of file for saving the file in the same folder

merger.close()