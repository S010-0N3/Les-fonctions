###Tokenization du vocabulaire :

vocabulary = open("dictionnaire.txt","r",encoding="utf-8").read()


### on va creer une liste de mots:
tokenization_vocabulary = vocabulary.split(" ")


###remplacement des caracteres speciaux :
f = open("texte.txt","r",encoding="utf-8")
text_string = f.read()


##method replace j'enleve la ponctuation 
text_string = text_string.replace(",","")
text_string = text_string.replace(".","")
text_string = text_string.replace("'","")
text_string = text_string.replace("Ã©","e")
text_string = text_string.replace("Ã","á")
text_string = text_string.replace("\n","")

print(text_string)
