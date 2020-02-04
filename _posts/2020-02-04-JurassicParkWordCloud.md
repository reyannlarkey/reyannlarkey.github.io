---
title: 'Creating a Word Cloud from the Jurassic Park Movie Script'
date: 2020-02-04
permalink: /posts/2020/02/jurassic_word_cloud/
tags:
  - Word Cloud
  - PIL
  - Scipy
  - Jurassic Park
---
Making a word cloud using Python


<p align="center">
  <img src="../../../../images/word_cloud_jurassic2.png" alt="Word Cloud" style="width:30%" />
</p>

<!--
<div style="text-align:center">


<iframe src="../../../../images/word_cloud_jurassic2.png" name="Word Cloud" height="500" width="500">You need a Frames Capable browser to view this content.</iframe>
</div>
-->


The Jurassic Park movie script can be found <a href = "https://www.springfieldspringfield.co.uk/movie_script.php?movie=jurassic-park">here</a>: 


Among other libraries, I used the <a href= "http://amueller.github.io/word_cloud"/> WordCloud </a> library to create this word cloud. 

### Start by importing all the packages needed:

```python
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import string
from scipy.ndimage import gaussian_gradient_magnitude
%matplotlib inline
```

### Next read the file containing the script and parse out the words:

```python
script_file = 'data/JurassicPark-Final.txt'

with open(script_file,'r') as f:
    lines = f.readlines()
    for line in lines:
	words = line.split()
	for word in words:
	    exclude = set(string.punctuation)
	    stripped_word = ''.join(ch for ch in word if ch not in exclude) # Exclude punctuation
	    if stripped_word != "":
	        word_list.append(stripped_word)

text = " ".join(word for word in word_list) #this is now a huge string containing the entire script!

```

### Now we need to get the logo and find the edges:

```python
logo_mask = np.array(Image.open("img/logo_large.png"))
mask = logo_mask # left over from some other testing


edges = np.mean([gaussian_gradient_magnitude(mask[:, :, i] / 255., 2) for i in range(3)], axis=0)
mask[edges > 0.08] = 255

plt.imshow(mask)
plt.show()
```

<img src="../../../../images/logo_large.png" alt="Jurassic" style="width:30%">









