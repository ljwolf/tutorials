#Mapping Political Data

Levi John Wolf
ljw2@asu.edu

This workshop will cover how to map data in QGIS, along with how to use some
elementary spatial operations in QGIS. For starters, install QGIS or open it on
the GIS lab computers. To open things on the GIS lab computers, first, log in
with your ASURITE account. This will pop you into the default OSX session.
Then, find QGIS using Spotlight or by looking in the Applications folder. Once
located, double click the icon to run the program. 

If you would rather install this on your own computer:

###Windows

Grab the [Windows](https://www.qgis.org/en/site/forusers/download.html) installer from the website. 

###Mac OSX

There are two options. First, you could use the William Kyngesburye's
[kyngchaos](www.kyngchaos.com/software/qgis) package repository. However, it
might be better if you used [Homebrew](http://brew.sh), which would manage all
of the dependencies for you. To install using Homebrew, first install homebrew
using the command given on the Homebrew website. To run this command, you need
to paste it at a Terminal command prompt. To open Terminal, use Spotlight to
search for "Terminal.app" and run that. Then, once you've installed homebrew, type: 

```
brew update && brew tap osgeo/osgeo4mac && brew install qgis
```

The program will grab the qgis dependencies and install them, hopefully without
any intervention needed.

##Data

The data is [here](http://public.asu.edu/~lwolf2/classes/polgeo/data.zip).
