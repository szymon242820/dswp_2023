text = input('Podaj jakiś tekst: ')
text = list(dict.fromkeys(list(text.casefold().replace(' ', ''))))
print(text)
text.sort()
print(text)