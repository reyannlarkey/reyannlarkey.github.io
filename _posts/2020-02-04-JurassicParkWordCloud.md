---
title: 'Creating a Word Cloud Using Python'
date: 2020-02-04
permalink: /posts/2020/02/jurassic_word_cloud/
tags:
  - Word Cloud
  - PIL
  - Scipy
  - Python
  - Jurassic Park
---
Making a word cloud from the Jurassic Park (1993) Script with Python.


<p align="center">
  <img src="../../../../images/word_cloud_jurassic2.png" alt="Word Cloud" style="width:50%" />
</p>


The Jurassic Park movie script can be found <a href = "https://www.springfieldspringfield.co.uk/movie_script.php?movie=jurassic-park">here</a>: 


Among other libraries, I used the <a href= "http://amueller.github.io/word_cloud"> WordCloud </a> library to create this word cloud. 

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


### Create the Word Cloud
```python
# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["youre", "Theyre", "Ill", "well","Im","Thats", "Id","Dont", "Theres","Ive",
                 "Didnt","Hes"]) #ignore some boring words

# Create a word cloud image
wc = WordCloud(stopwords = stopwords,max_words=5000, mask=mask, max_font_size=100, random_state=20,
               relative_scaling=0.5)

# Generate a wordcloud
wc.generate(text)
```

### Finally, add some coloring and make it look nice:
```python
#create coloring from image
image_colors = ImageColorGenerator(mask)
wc.recolor(color_func=image_colors)
plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation="bilinear")


image = Image.open('img/logo_large.png')# add the logo back in so you can see it a little better
plt.imshow(image, alpha=0.2)

plt.axis("off")
```

### If you want to save your images:
```python
wc.to_file("img/word_cloud_jurassic.png") #only saves word cloud
plt.savefig("img/word_cloud_jurassic2.png", bbox_inches = 'tight') # saves everything
```

<p align="center">
  <img src="../../../../images/word_cloud_jurassic2.png" alt="Word Cloud" style="width:100%" />
</p>

Try it yourself with an interactive Jupyter Notebook here: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/reyannlarkey/JurassicParkWords.git/master?filepath=jurassic%2Fjurassic.ipynb)







