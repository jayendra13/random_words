import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

df = pd.read_csv('/Users/Nisarg/Desktop/lst', header=None)
v1 = df[0].as_matrix()

words = v1[np.random.randint(0, high=len(v1), size=(10,))]

for w in words:
	r = requests.get('http://dictionary.reference.com/browse/%s?s=t'%(w))
	soup = BeautifulSoup(r.text, 'html.parser')
	results = soup.findAll('div', attrs={'class': 'def-content'})
	
	print '*********************'
	print w
	for r in results:
		print '\t' + r.getText().strip()
		
	r = requests.get('http://www.gujaratilexicon.com/dictionary/english-to-gujarati/%s*/'%(w))
	soup = BeautifulSoup(r.text, 'html.parser')
	results = soup.findAll('div', attrs={'class': 'meaning'})
	for r in results:
		print '\t' + r.getText().strip()