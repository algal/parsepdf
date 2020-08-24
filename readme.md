# ParsePDF

A simple command line script to extract text from a certain page number and rect coordinates in a pdf

Just a wrapper over ImageMagick's `convert` and the `tesseract` command, which are both installable via brew.

This is not a complex script.

# Usage

```
# Go to page 5 and parse the text in rect of width 360, height 21, x-offset 19, y-offset 109, in the file foo.pdf
$ parsepdf.py 5 360x21+19+109 foo.pdf

# Same, but show some more information about the underlying calls:
$ parsepdf.py --verbose 5 360x21+19+109 foo.pdf
```

# Resources

https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
https://apple.stackexchange.com/questions/127997/using-automator-to-batch-crop-with-custom-coordinates-measurements/128000#128000
