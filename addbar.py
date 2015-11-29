#######################################################################
# Copyright 2013 Junghoon Kim
# jfkimberly@skku.edu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#######################################################################

from pyPdf import PdfFileWriter, PdfFileReader

# run from the command line
name = raw_input("Enter name of file (excluding '.pdf')\n")
namepdf = name + ".pdf"

# number of output channels
while True:
    try:
        channels = int(
            raw_input("How many output channels (usually 1 or 2)?\n"))
    except ValueError:
        print("Try 1 or 2")
    else:
        if 1 <= channels <= 2:
            break
        else:
            print("Try 1 or 2")

# output filename
outputfile = raw_input(
    "Output filename without '.pdf' (default: 'filename-addbar.pdf')?\n")

infoot = PdfFileReader(file(namepdf, "rb"))
outfoot = PdfFileWriter()

numPages = infoot.getNumPages()
print "document has %s pages." % numPages

if channels == 1:
    watermark = PdfFileReader(file("bar.pdf", "rb"))
if channels == 2:
    watermark = PdfFileReader(file("bar2.pdf", "rb"))

for pagenum in range(numPages):

    page = infoot.getPage(pagenum)
    page.mergePage(watermark.getPage(0))

    #    print page.mediaBox.getLowerRight_x(), page.mediaBox.getLowerRight_y()

    if channels == 1:
        page.trimBox.upperLeft = (62, 38)
        page.trimBox.lowerRight = (458, 434)
        page.cropBox.upperLeft = (62, 38)
        page.cropBox.lowerRight = (458, 434)

    elif channels == 2:
        page.trimBox.upperLeft = (43.5, 0)
        page.trimBox.lowerRight = (440, 793.5)
        page.cropBox.upperLeft = (43.5, 0)
        page.cropBox.lowerRight = (440, 793.5)

    outfoot.addPage(page)


if outputfile == '':
    outfootStream = file(name + "-addbar.pdf", "wb")
else:
    outfootStream = file(outputfile + ".pdf", "wb")

outfoot.write(outfootStream)
outfootStream.close()
