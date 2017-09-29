# info-retrieval
Project developed for Information Retrieval (MAB605) class at Federal University of Rio de Janeiro

## How to Run

### Prerequisites
* Linux 
* Download [collection](http://dcc.ufrj.br/~giseli/2017‐1/ri/trabalho1/colecao_teste.zip) and extract
* Download [queries](http://dcc.ufrj.br/~giseli/2017‐1/ri/trabalho1/consultas.txt)

### Install
```
sudo apt-get install python2.7
sudo apt-get install python-whoosh
sudo apt-get install python-bs4
sudo apt-get install python-nltk
```

### Run
* Extract the nltk.tar.gz to your user home directory
* Put the folder "colecao_teste" and the file "consultas.txt" previously downloaded in the same directory as "indexar.py" and "consultar.py"
* Run
```
    python indexar.py && python consultar.py
```
* The first command will take about two hours
* When the process finishes, check the results in the file "resultado.txt"
