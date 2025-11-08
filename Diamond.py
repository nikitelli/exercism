def rows(letter):

    if not 'A' <= letter <= 'Z':
        return []

    # Determine the diamond's dimensions
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = alphabet.find(letter)
    max_width = 2 * index + 1
    diamond_lines = []

    # Build the top half of the diamond (including the middle row)
    for i in range(index + 1):
        current_letter = alphabet[i]
        
        # 'A' row is special (no inner spaces)
        if i == 0:
            leading_spaces = (max_width - 1) // 2
            line = ' ' * leading_spaces + current_letter + ' ' * leading_spaces
        else:
            inner_spaces = 2 * i - 1
            leading_spaces = (max_width - (2 + inner_spaces)) // 2
            line = ' ' * leading_spaces + current_letter + ' ' * inner_spaces + current_letter + ' ' * leading_spaces
        
        diamond_lines.append(line)

    # Build the bottom half
    bottom_half = diamond_lines[:-1][::-1]
    
    # Combine the top and bottom halves
    full_diamond_lines = diamond_lines + bottom_half
    
    return full_diamond_lines

p = rows('D')
print(p)