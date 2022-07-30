from stegano import lsb
from textblob import TextBlob


print("\t Welcome To Translator and Steganographer.")
inp = input('Enter Message - \n')
print("Entered Text is - ",inp) #takes in the input
print("\nTranslated Statement is - \n")
blob = TextBlob(inp)            
trans = blob.translate(from_lang='en', to='fr') #translates input from english to french.
print(trans)    # prints translated string
# Better to use png than jpeg becuase of less loss chances, Following code is to hide Text in image.
secret = lsb.hide("C:/D - Drive/Python/Pyfolder/Projects/gou.png", trans) # Hides message in the image, necessary to give right path of the image
secret.save("gousec.png")
print("\nMessage Successfully hidden.")
print("\nHidden Statement within The Image Is - \n")


Hidden = lsb.reveal("C:/D - Drive/Python/Pyfolder/Projects/gousec.png")   # Reveals hidden message from within the image
print(Hidden)

orignal = blob.translate(from_lang='fr', to='en')            #Translates the hidden message back to orignal language.

print("Orignal Statement Was -\n",orignal)
print("\t Thank You For Using This Program.Peace Out.")



