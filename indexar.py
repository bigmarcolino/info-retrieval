import codecs
from os.path import exists
from os import mkdir, listdir  
from sys import setrecursionlimit
from string import punctuation
from whoosh.index import create_in
from whoosh.fields import STORED, TEXT, Schema
from bs4 import BeautifulSoup, SoupStrainer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

setrecursionlimit(30000)
stop_words = set(stopwords.words("portuguese"))

def text_cleaner(text):
	cleaned_text = word_tokenize(text)
	return " ".join([RSLPStemmer().stem(x) for x in cleaned_text if (x not in punctuation and x not in ["\'\'", "``", "..."] and x.lower() not in stop_words)])

if not exists("indexdir"):
    mkdir("indexdir")

schema = Schema(doc_no = STORED, text = TEXT)
ix = create_in("indexdir", schema)
writer = ix.writer(limitmb = 2048, multisegment = True)
only_doc = SoupStrainer("doc")
doc_atual = 1

for filename in listdir("colecao_teste"):
    if filename.endswith(".sgml"):
    	diretorio = "colecao_teste/" + filename
    	docs = BeautifulSoup(codecs.open(diretorio, encoding = 'latin-1'), "lxml", parse_only = only_doc)

    	for doc in docs:
            doc_no = doc.find('docno').string
            text = text_cleaner(doc.find('text').string)

            writer.add_document(doc_no = doc_no, text = text)
            print(str(doc_atual) + " de 103913")
            doc_atual += 1

writer.commit()