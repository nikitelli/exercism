def translate(text):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    #If a word begins with a vowel, or starts with "xr" or "yt", it adds an "ay" sound to the end of the word.
    if (text[0] in vowels or
        text.startswith("xr") or
        text.startswith("yt")):
            return text + "ay"

    new_s = ''

    # ------------------------------------------------------------------

    # If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) 
    # and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
    if text[0] == 'q' and text[1] == 'u':
        new_s = text[2:] + text[0] + text[1] + 'ay'
        return new_s

    if text[0] in consonants and text[1] == 'q' and text[2] == 'u':
        new_s = text[3:] + text[0] + text[1] + text[2] + 'ay'
        return new_s

    # ------------------------------------------------------------------

    # Check for "qu" starting after zero or more consonants
    for i in range(len(text)):
        if text[i:i+2] == "qu":
            # If "qu" is at the very beginning (i=0)
            if i == 0:
                return text[2:] + "quay"
            # If "qu" is preceded by consonants
            else:
                consonant_prefix = text[:i]
                return text[i+2:] + consonant_prefix + "quay"
        # If we encounter a vowel before "qu", this rule doesn't apply
        # (assuming "qu" is the *first* "qu" sequence after consonants)
        if text[i] in consonants:
            break # Exit if a consonant is found, meaning no initial consonant + qu pattern

    # ------------------------------------------------------------------

    # If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
    # Find the index of the first vowel
    word_lower = text.lower()
    # Initializes a variable to store the index of the first vowel found. If no vowel is found, it remains -1.
    first_vowel_index = -1
    # loop iterates through the lowercase word, getting both the index (i) and the character (char).
    for i, char in enumerate(word_lower):
        if char in vowels:
            first_vowel_index = i
            break

    # If no vowel is found (e.g., "rhythm", "sh"), or if the word starts with a vowel
    # (Word has no vowels or is all consonants):
    if first_vowel_index == -1:
        # If the word is entirely consonants (e.g., "rhythm"), move all of it
        # Or if it's an empty string/single consonant like 'b'
        if word_lower and word_lower[0] not in vowels: # Ensure it's not an empty string and starts with a consonant
             return text + "ay" # Special case for "rhythm" - just add 'ay' to the whole word

    # If the word begins with one or more consonants
    consonant_prefix = text[0:first_vowel_index]
    rest_of_word = text[first_vowel_index:]

    return rest_of_word + consonant_prefix + "ay"

    # if text[0] in consonants:
    #     new_s = text[1:] + text[0]
    #     print("1 :" + new_s)
    #     if text[1] in consonants:
    #         new_s = new_s[1:] + text[1]
    #         print("2 :" + new_s)
    #         if text[2] in consonants:
    #             new_s = new_s[1:] + text[2]
    #             print("3 :" + new_s)
    # new_s += 'ay'
    # return new_s

    # ------------------------------------------------------------------

    # If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y" to the end of the word,
    # and then add an "ay" sound to the end of the word.

    word_lower = text.lower()  # Work with lowercase for consistent matching

    # The 'y' must be preceded by at least one consonant,
    # so we start checking from the second character (index 1).
    for i in range(1, len(word_lower)):
        # Check if the current character is 'y'
        if word_lower[i] == 'y':
            # Check if all characters from the beginning up to 'y' (exclusive) are consonants
            consonant_prefix_found = True
            for j in range(i):
                if word_lower[j] in vowels:
                    consonant_prefix_found = False
                    break # A vowel was found before 'y', so this rule doesn't apply here
            
            if consonant_prefix_found:
                # 'y' is preceded by only consonants from the start of the word
                consonant_prefix = text[0:i]  # Original word's consonants before 'y'
                rest_of_word = text[i:]       # Original word from 'y' onwards
                return rest_of_word + consonant_prefix + "ay"
        
        # If the current character is a regular vowel (not 'y')
        # and it's encountered before a 'y' that follows consonants,
        # then this rule doesn't apply to the word.
        elif word_lower[i] in vowels:
            break # Exit the loop, the pattern for this rule is broken


r = translate("rhythm")
print(r)