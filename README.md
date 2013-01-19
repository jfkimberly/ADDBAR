ADDBAR
======

ADDBAR is a python script which automatically crops the image portion of the pdf file(s) of atomic force microscopy (AFM) images produced by NanoScope Software (Veeco Instruments Inc.). In addition, a scale bar whose length is one-tenth of the width of the image is superimposed in the bottom-right corner.


Dependencies
------------

All parsing, cropping, and manipulation of the input pdf file is done using the [pyPDF](http://pybrary.net/pyPdf/) library. No other dependencies are required.


Usage
-----

At the command line, type

`$ python addbar.py
> Enter name of file (excluding '.pdf')`

Enter the name of the pdf file (without typing '.pdf'). The file may be multiple pages. For example if you have a file named *example.pdf*, type *example* and a file named *example-addbar.pdf*, with all the cropped images and added scale bars, will be produced.