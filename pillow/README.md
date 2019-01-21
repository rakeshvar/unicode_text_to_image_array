Rendering Indic Text Using Pillow in Python
====

This uses the following libraries

 1. Freetype
 2. Harfbuzz
 3. Fribidi
 4. GTK Doc Tools
 5. Raqm

These are the steps one need to follow on `Ubuntu 18.04 (Bionic Beaver)` with `Python 3.6.7`

 1. `sudo pip3 install -U Pillow` installs `5.4.1` or newer
 2. `sudo apt-get install libfreetype6-dev libharfbuzz-dev libfribidi-dev gtk-doc-tools`
 3. Install `libraqm` as described there (HOST-Oman/libraqm) using `configure`, `make`, `make install`
 4. `sudo ldconfig` This step was needed!
 5. Run the test script (Make sure the fonts are installed `sudo apt install fonts-indic`)
