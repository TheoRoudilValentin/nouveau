import os
os.mkdir("c:/chemin") #crée le dossier "chemin" dans c
print(os.getcwd()) #renvoie le répertoire actuel

from pathlib import Path
os.path.exists("c:/bla") #renvoie True si le chemin existe ou false sinon
not os.path.exists("c:/bla") #renvoie donc l'inverse

import html
html.unescape(s) #Convert all named and numeric character references (e.g. &gt;, &#62;, &#x3e;) 
#in the string s to the corresponding Unicode characters. This function uses 
#the rules defined by the HTML 5 standard for both valid and invalid character references, 
#and the list of HTML 5 named character references.

import re
re.sub('abc','',input) #replace abc by nothing (so delete) in input

zip(x,y) #ça va matcher les éléments de x et y un par un, si ils ont la même dim

from spacy.util import minibatch #fonction qui sert pour l'itération
minibatch(x,k) #crée des petits groupes de dim k au sein de x à partir desquels on peut itérer dans une boucle

from joblib import Parallel, delayed
Parallel(n_jobs="The maximum number of concurrently running jobs",prefer=)
delayed()

#%%
from functools import partial
def f(x,y):
    return x**2+y
f(2,1)

h=partial(f,1)

from joblib import Parallel, delayed
d=delayed(h)
t=(d(i) for i in range(1,10))
ex=Parallel(n_jobs=1)
ex(t)
#%%

import spacy
spacy.load('fr_core_news_sm',disable=["parser","ner"]) #charge un modèlede de nlp en français 
#il faut l'avoir installé d'abord
!pip install spacy
!python -m spacy download fr_core_news_sm

#tokenizer = segment text into tokens
#tagger = assign POS tags
#parser = assign dependency labels
#ner = detect and label named entities

#%%
text="bla bob"
text.split()
text=' '.join(text.split())
text
# %%
