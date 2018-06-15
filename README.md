# edit-distance

This program measures the "edit distance" between two strings, that is, the minimal number of additions, deletions, and/or edits necessary to transform one string into the other.

/templates: This folder contains HTML files of the web application

/static: This folder contains a CSS file of the web application

score: This python file parses two command-line arguments, FILE1 and FILE2, the files to compare. The program then tries to read the contents of those files into strings, and passes those strings to a function "distances"

helpers.py: In this file is a function called distances that takes two strings as arguments, a and b, and returns the edit distance between one and the other.

application.py: This file implements a web application that allows you to visualize the edit distance between two strings as well as the operations necessary to transform one into the other at minimal cost.
