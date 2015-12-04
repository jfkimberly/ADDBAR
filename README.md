ADDBAR
======

ADDBAR is a python script which automatically crops the image portion of the pdf
file(s) of atomic force microscopy (AFM) images produced by NanoScope Software
(Veeco Instruments Inc.). In addition, a scale bar whose length is one-fifth of
the width of the image is superimposed in the bottom-right corner.


Dependencies
------------

All parsing, cropping, and manipulation of the input pdf file is done using the
[pyPDF](http://pybrary.net/pyPdf/) library. No other dependencies are required. 

All dependencies can be installed using `pip`. `pip` does not come pre-installed  with the python virtual machine, so you need to install it manually.

* Install pip (if you do not have it installed)

`# yum install python-pip`
	
or 

`$ sudo apt-get install python-pip`
	
for linux machines.

* Upgrade `pip`.

`$ sudo pip install pip --upgrade`

* Install all required dependencies by typing
   
`$ pip install -r requirements.txt`


Usage
-----

At the command line, type

```
$ python addbar.py
> Enter name of file (excluding '.pdf')
```

Enter the name of the pdf file (without typing '.pdf'). The file may be multiple
pages. For example if you have a file named *example.pdf*, type *example*.

```
> How many output channels (usually 1 or 2)?
1
```

This question asks how many output channels there are in the pdf file. For
instance, if each page has only the height data, the number of output channels
is `1`. If there are 2 output data channels, such as the height and amplitude
data in the pdf file, then the number of output channels is `2`.

```
> Output filename without '.pdf' (default: 'example-addbar.pdf')?
```

Type the name of the output file you want. The default (just pressing `Enter`)
is the name of the input file with the `-addbar` suffix appended, in which
case, a file named *example-addbar.pdf*, with all the cropped images and scale
bars added, will be produced.
