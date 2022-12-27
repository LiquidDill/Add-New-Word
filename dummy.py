words = []

def add_new_word(number):
    words.append(number)

while True:
    stars = input('enter word: ')
    stars = stars.strip()
    stars = stars.lower()
    add_new_word(stars)
    print(words)