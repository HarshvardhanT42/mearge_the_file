# mearge_the_file
in this code we use PyPDF2 to use the operation to mearge the fils 
This Python script merges multiple PDF files into a single PDF using the `PyPDF2` library.

### Explanation:

1. **Importing `PdfMerger`:** The script imports `PdfMerger` from the `PyPDF2` library to handle the merging of PDFs.
2. **Creating a Merger Object:** `merger = PdfMerger()` initializes a PDF merger object.
3. **List of PDF Files:** The list `pdf_files` contains the paths of the PDF files to be merged. You need to specify the file names and their paths.
4. **Merging PDFs:** The `for` loop iterates over the list of PDF files, appending each one to the merger.
5. **Writing the Merged PDF:** `merger.write("meargpdf/123.pdf")` saves the merged PDF as `123.pdf` in the specified folder.
6. **Closing the Merger:** Finally, `merger.close()` ensures that the merger object is properly closed and the changes are saved.

### Example:
If you merge `1.pdf`, `2.pdf`, and `3.pdf` from the directory `"meargpdf"`, they will be combined into a single file called `123.pdf`.

Output:
```
Files 1.pdf, 2.pdf, 3.pdf merged into 123.pdf
```

This script is useful when you need to combine multiple PDFs into one file. Just update the file paths as needed!
