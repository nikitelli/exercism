def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.
 
    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.
 
    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    liste = ' :: '.join(vocab_words)
    prefix = vocab_words[0]
    preliste = ''
    for code_point in vocab_words[1:]:
        preliste = preliste + " " + (prefix + code_point)

    semifinal = vocab_words[0] + preliste
    semifinal = semifinal.split()
    print(semifinal)
    final = ' :: '.join(semifinal)
    print(final)

#input_data = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete']
#make_word_groups(input_data)

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
 
    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.
 
    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    print(word[-4:])
    ness_start = word.rfind('ness')
    before_ness = word[:ness_start]
    print(before_ness)
    last_char = (before_ness[-1])
    if last_char.lower() in {'a', 'e', 'i', 'o', 'u'}:
        print('Hit!: ' + word)
        replaced = before_ness[:-1] + 'y'
        print(replaced)
        return replaced
    
    print('no Hit!: ' + word)
    print(before_ness)
    return before_ness

#remove_suffix_ness('heaviness')

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    list = sentence.split(' ')
    adj = list[index]
    if adj[-1] == '.':
        print(adj + 'has a .')
        adj = adj[:-1]
        print(adj + 'en')
        return adj
    
    print(adj + 'en')
    return adj

adjective_to_verb('I need to make that bright.', -1)
adjective_to_verb('It got dark as the sun set.', 2)
