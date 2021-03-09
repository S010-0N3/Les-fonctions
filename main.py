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


# on va maintenant creer une fonction qui nous permetra de nettoyer la ponctuation directement.

def clean_text(string_value):
  clean_value = string_value.replace(",","")
  clean_value = clean_value.replace(".","")
  clean_value = clean_value.replace("'","")
  clean_value = clean_value.replace("Ã©","e")
  clean_value = clean_value.replace("Ã","á")
  clean_value = clean_value.replace("\n","")
  # et si on enlever les Majuscule ?
  clean_value= clean_value.lower()
  #
  return(clean_value)


text_ok = clean_text(text_string)
print(text_ok)


