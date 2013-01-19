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

# 
name = raw_input("Enter name of file (excluding '.pdf')\n")
namepdf = name + ".pdf"

infoot = PdfFileReader(file(namepdf, "rb"))
outfoot = PdfFileWriter()

numPages = infoot.getNumPages()
print "document has %s pages." % numPages

for i in range(numPages):
    page = infoot.getPage(i)

    watermark = PdfFileReader(file("bar.pdf", "rb"))
    page.mergePage(watermark.getPage(0))

#    print page.mediaBox.getLowerRight_x(), page.mediaBox.getLowerRight_y()

    page.trimBox.upperLeft = (62, 38)
    page.trimBox.lowerRight = (458, 434)
    page.cropBox.upperLeft = (62, 38)
    page.cropBox.lowerRight = (458, 434)
    outfoot.addPage(page)

outfootStream = file(name + "-addbar.pdf", "wb")
outfoot.write(outfootStream)
outfootStream.close()
