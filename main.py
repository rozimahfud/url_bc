import torch
import numpy as np
import torch.nn as nn
from js_to_bc import js_to_bc
from crawler import getJsUrl
from crawler import getJsCode
from crawler import getInsideCode
from model.DPCNN import DPCNN
from gensim.models import Word2Vec

torch.manual_seed(1)
torch.manual_seed(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
max_len = 200000
word_embedding = 100

url = "http://www.iamgameaddict.com/"
modelPath = "model_DPCNN.pt"

# import dictionary
def getDictionary():
	word2vec_model = Word2Vec.load("model_w2v_gensim")
	w2v_vectors = word2vec_model.wv.vectors
	dictionary = {}
	for idx, word in enumerate(word2vec_model.wv.index2word):
		dictionary[word] = idx
	vocab_size = len(dictionary)
	return dictionary, vocab_size, w2v_vectors

def makePadding(s):
	padded = np.zeros((max_len,), dtype=np.int64)
	if len(s) > max_len:
		padded[:] = s[:max_len]
	else:
		padded[:len(s)] = s
	return padded

def main():
	model = DPCNN().to(device)
	model.load_state_dict(torch.load(modelPath))
	dictionary, vocab_size, w2v_vectors = getDictionary()
	embeds = nn.Embedding(vocab_size,word_embedding).to(device)
	embeds.from_pretrained(torch.FloatTensor(w2v_vectors))
	
	list_js_code = getInsideCode(url)
	for subUrl in getJsUrl(url):
		list_js_code.append(getJsCode(subUrl))

	print("Number of JS file: ",len(list_js_code))
	prediction = []
	score_output = []
	for idx, js_code in enumerate(list_js_code):
		if js_code:
			bytecode = js_to_bc(js_code)
			model_input = [dictionary[x] for x in bytecode if x in dictionary]
			model_input = torch.tensor(makePadding(model_input)).to(device)
			model_input = embeds(model_input)
			model_input = model_input.unsqueeze(0).unsqueeze(1)
			predicted_label, output = model.predict(model_input) # 0=benign ; 1=malicious
			prediction.append(predicted_label)
			score_output.append(output)


if __name__ == "__main__":
	main()