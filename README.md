# RU Hacks 2020 : Resonance.ai, an AI-powered companion for podcast-lovers

<p align="center">
  <img src="logo.png" width="300">
</p>
<br>
Podcasts have been exploding with popularity lately, and it's getting harder to sift through it all to get to the content you really care about. Resonance.ai is our attempt at creating the podcast companion we've always wanted. Resonance.ai lets you browse through and play all your favorite podcasts, and create your own snippets of your favorite parts for those key takeaways. In addition, Resonance.ai leverages state-of-the-art natural language processing (NLP) artifical intelligence to find the best matches to your taste as well as to craft succinct, thoughtful summaries of podcasts before sinking in the 30 minutes they would otherwise demand.
<br><br>
<i>Can you hear the future? It's Resonance.ai, using cutting edge artificial intelligence to help you enjoy and discover podcasts just for you.</i>

<br><br>

The AI pipeline is contained entirely in https://github.com/salehi2/RUhacks/blob/master/RU_Hacks_2020_podcast_processing.ipynb . See here for implementation of the pipeline from podcast audio to embedding vectors. BERT encoding is in a separate script, 'get_embeddings.py'

How to view the summaries and podcast similarities for the 14 podcasts used in demo:<br><br>

```python
import pickle

summaries = pickle.load(open('summaries.pkl', 'rb'))                # List of podcast summaries
cosine_distances = pickle.load(open('cosine_distances.pkl', 'rb'))  # Dictionary with key:val = podcast_id:list*

# *list indices are podcast_id and their contents is the cosine distance from the query podcast_id (key) and that podcast_id
```

<br><br>
How to run the GUI:

Clone the git repository to a directory 'dir',

Navigate to directory 'dir\RUhacks-master\Prototype - Player\Protov006\Protov005\',

Download the podcast .WAV files (over 1GB!) from https://drive.google.com/open?id=1bi9MVp3bBL5s6Y1ZzEA8rWZJ5VjtHInk ,

Unzip them into the same directory,

then run, in a shell with Python 3+ installed:

```python
python Hackathon.py
```
<br><br>
We use https://github.com/hanxiao/bert-as-service to generate our BERT embeddings.
