Refer to the html documentation in the help/ subdirectory.

Kodos is a Python Gui for creating and debugging regex. I was using this up to about two years ago and it was availabled on Fedora. Recently I wanted to use it again and could no longer find it available. Searching around the net, I found that it was not updated to work with Python3.x and PyQt5 and as a result was dropped in Fedora. I therefere decided to port it for my own use.

Building : python3 setup.py build
Install  : python3 setup.py install

A single binary can be built with:

pyinstaller --onefile kodos.py

