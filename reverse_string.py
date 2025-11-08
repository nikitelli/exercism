def reverse(text):

    liste = []
    reversed_text = ''

    if text == '':
        return text
    
    for i in text:
        liste.append(i)

    liste.reverse()

    for i in liste:
        reversed_text += i

    return reversed_text

p = reverse('robot')
print(p)