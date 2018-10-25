### Task ### How to download youtube videos in python through link :-
clipconverter.cc
Notes: 

Pytube is a python library to download youtube videos

For this porpose we actually need to download windows     anaconda because it has some supercore powers to download youtube videos.

how to create different python environment in conda on windows
:- conda create --name youtube python=2.7.8
activate env :- activate youtube
then : pip install pytube

to check PyTube is installed or not : pip list | grep PyTube

if PyTube is not working properly you can use :

git clone https://github.com/nficano/pytube.git && cd pytube
setup.py build
sudo setup.py install	


