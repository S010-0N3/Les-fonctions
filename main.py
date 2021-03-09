###Tokenization du vocabulaire :

vocabulary = open("dictionnaire.txt","r",encoding = "utf-8").read()
print(vocabulary)

### on va creer une liste de mots:
tokenization_vocabulary = vocabulary.split(" ")
print(tokenization_vocabulary)

###remplacement des caracteres speciaux :
f = open("texte.txt","r",encoding="utf-8")
text_string = f.read()
print(text_string)
