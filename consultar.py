from string import punctuation
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from bs4 import BeautifulSoup, SoupStrainer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

stop_words = set(stopwords.words("portuguese"))

def text_cleaner(text):
	cleaned_text = word_tokenize(text)
	return " ".join([RSLPStemmer().stem(x) for x in cleaned_text if (x not in punctuation and x not in ["\'\'", "``", "..."] and x.lower() not in stop_words)])

ix = open_dir("indexdir")
only_top = SoupStrainer("top")
tops = BeautifulSoup(open("consultas.txt", encoding = 'latin-1'), "lxml", parse_only = only_top)

with open("resultado.txt","w") as file:
	for top in tops:
		with ix.searcher() as searcher:
			consulta = top.find('pt-title').string
			consulta_limpa = text_cleaner(consulta)
			num_consulta = top.find('num').string.replace(" ", "")
			ordenacao = 0

			query = QueryParser("text", ix.schema).parse(consulta_limpa)
			results = searcher.search(query, limit = 100)

			print("Consulta " + num_consulta)
			
			for hit in results:
				file.write(num_consulta + " Q0 " + hit["doc_no"] + " " + str(ordenacao) + " " + str(hit.score) + " MarcusViniciusIbraim_GuilhermeGobbi\n")
				ordenacao += 1

				if len(results) == ordenacao:
					file.write("\n")