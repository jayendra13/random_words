import sys
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from nltk.corpus import wordnet as wn

show_english = True
show_gujrati = True
show_sentences = True
lst = []

def scrape(words):

	for w in words:
	
		if w not in lst:
			print w + ' is not in our database'
		
		r1 = requests.get('http://dictionary.reference.com/browse/%s?s=t'%(w))
		soup1 = BeautifulSoup(r1.text, 'html.parser')
		results1 = soup1.findAll('div', attrs={'class': 'def-content'})
		p1 = soup1.findAll('span', attrs={'class': 'pron ipapron'})
		if len(p1) == 0:
			p1 = ''
		else:
			p1 = p1[0].getText().strip()
		
		results3 = soup1.findAll('p', attrs={'class': 'partner-example-text'})
	
		r2 = requests.get('http://www.gujaratilexicon.com/dictionary/english-to-gujarati/%s*/'%(w))
		soup2 = BeautifulSoup(r2.text, 'html.parser')
		results2 = soup2.findAll('div', attrs={'class': 'meaning'})
		p2 = soup2.findAll('div', attrs={'class': 'sw-3'})
		if len(p2) == 0:
			p2 = ''
		else:
			p2 = p2[0].getText().strip()

		print '**********************************'
		print w + ' (' + p1 + ' ' + p2 +')'

		if show_gujrati:
			for r in results2:
				print '\t' + r.getText().strip()
		print '\n'
	
		if show_english:
			for r in results1:
				print '\t' + r.getText().strip()
		print '\n'
		
		if show_sentences:
			l = 10000
			fs = ''
			for r in results3:
				s = r.getText().strip()
				if len(s)<=l:
					fs = s
			print '\t## ' + fs
		print '\n'

def use_wordnet(words):

	for w in words:
	
		if w not in lst:
			print w + ' is not in our database'
		
		r2 = requests.get('http://www.gujaratilexicon.com/dictionary/english-to-gujarati/%s*/'%(w))
		soup2 = BeautifulSoup(r2.text, 'html.parser')
		results2 = soup2.findAll('div', attrs={'class': 'meaning'})
		p2 = soup2.findAll('div', attrs={'class': 'sw-3'})
		if len(p2) == 0:
			p2 = ''
		else:
			p2 = p2[0].getText().strip()

		print '**********************************'
		#print w + ' (' + p1 + ' ' + p2 +')'
		print w

		if show_gujrati:
			for r in results2:
				print '\t' + r.getText().strip()
		print '\n'
	
		if show_english:
			syns = wn.synsets(w)
			for s in syns:
				print '\t' + ', '.join(s.lemma_names())
			print '\t' + s.definition()
		print '\n'
		

if __name__ == '__main__':

	
	df = pd.read_csv('lst', header=None)
	v1 = df[0].as_matrix()
	lst = v1.tolist()
	
	print sys.argv
	if len(sys.argv)>1:
		words = sys.argv[1:]
	else:
		words = v1[np.random.randint(0, high=len(v1), size=(10,))]
		print words

	show_english = True
	show_gujrati = True
	show_sentences = True

	
	use_wordnet(words)