def is_pangram(sentence):
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  s1 = sentence.lower()
  i = 0
  for letter in letters:
    if letter in s1:
      i += 1

  print(i)

  if i == 26:
      return true
  else:
      return False

#is_pangram("The quick brown fox jumps over the lazy dog.")
#is_pangram("abce")
#is_pangram("")
is_pangram("abcdefghijklmnopqrstuvwxyz")