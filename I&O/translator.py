from translate import Translator

translator = Translator(to_lang="zh")
translation = translator.translate("Hello Juma.")
print(translation)

data = open("translator.txt")
full_data = data.read()

trans = translator.translate(full_data)
print(trans)
