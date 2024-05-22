# Amelia's Science Utility Scripts

I will forget about these unless I archive them and it may also be useful for you.


## To gif

Generating animations in matplotlib can be a little annoying, I'm lazy and therefore I want to quickly combine 
a folders worth of images into a gif. By default only takes in number .png and saves the gif as directoryname.gif.

Requires imageio to be installed.

usage: ```python to_gif.py [directory] ```

## To video
It's easier to just run this shell command:
```ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y movie.mp4```

## Clean BibTex

Combine a .bib and a .tex file to create a new .bib that contains only entries referenced in the .tex
and alphabetises. Also removes any non-ascii script from the .bib as many latex interpreters get annoyed
with this.

Requires unidecode to be installed

usage:
```clean_bibtex.py example.bib example.tex output.bib```
