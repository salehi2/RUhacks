import pickle
from bert_serving.client import BertClient

bc = BertClient(output_fmt='list')

summaries = pickle.load(open('summaries.pkl', 'rb'))

embeddings = []

for s in summaries:
	sentences = s.split('.') # split by sentence
	sentences = [i for i in sentences if len(i) > 0] # remove empty sentences
	#print(sentences[:3])
	emb = bc.encode(sentences)
	embeddings.append(emb)



pickle.dump(embeddings, open('summary_emb.pkl', 'wb'))
