# A dictionary to map each color name to its corresponding digit.
COLOR_CODES = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}

def label(colors):
    """
    Calculates the resistance value in ohms from a list of three color bands
    and returns a formatted string with metric prefixes.

    Args:
        colors (list): A list containing three strings, each representing a color band.
                       (e.g., ['orange', 'orange', 'red']).

    Returns:
        str: The resistance value as a formatted string (e.g., "33 kiloohms"),
             or an error message if an invalid input is provided.
    """
    # Check for invalid input length.
    if len(colors) > 3:
        return "Error: Too many color bands provided. This program only handles 3 bands."
    if len(colors) < 3:
        return "Error: Too few color bands provided. This program requires 3 bands."    

    # Convert color names to lowercase to make the function case-insensitive
    band1 = colors[0].lower()
    band2 = colors[1].lower()
    band3 = colors[2].lower()

    # Check if all color bands are valid
    if band1 not in COLOR_CODES or band2 not in COLOR_CODES or band3 not in COLOR_CODES:
        return "Error: Invalid color name provided."

    # Get the numerical value for the first two bands.
    digit1 = COLOR_CODES[band1]
    digit2 = COLOR_CODES[band2]

    # Combine the first two digits to form the base resistance value.
    base_value = (digit1 * 10) + digit2

    # Get the multiplier value from the third band. This represents the power of 10.
    multiplier_power = COLOR_CODES[band3]
    final_value = base_value * (10 ** multiplier_power)

    # Now, format the final_value with metric prefixes
    # Check for kiloohms (1,000)
    if final_value >= 1_000 and final_value < 1_000_000:
        return f"{final_value // 1000} kiloohms"
    # Check for megaohms (1,000,000)
    elif final_value >= 1_000_000 and final_value < 1_000_000_000:
        return f"{final_value // 1_000_000} megaohms"
    # Check for gigaohms (1,000,000,000)
    elif final_value >= 1_000_000_000:
        return f"{final_value // 1_000_000_000} gigaohms"
    # Otherwise, return the value in ohms
    else:
        return f"{final_value} ohms"
    
# --- Example Usage ---

# Example 1: orange-orange-black -> 33 ohms
value1 = label(['orange', 'orange', 'black'])
print(f"['orange', 'orange', 'black'] -> {value1}")

# Example 2: orange-orange-red -> 3.3 kiloohms
value2 = label(['orange', 'orange', 'red'])
print(f"['orange', 'orange', 'red'] -> {value2}")

# Example 3: orange-orange-orange -> 33 kiloohms
value3 = label(['orange', 'orange', 'orange'])
print(f"['orange', 'orange', 'orange'] -> {value3}")

# Example 4: A more complex example, like brown-green-yellow
# Brown=1, Green=5, Yellow=4. Value is 150000 ohms, should be 150 kiloohms
value4 = label(['brown', 'green', 'yellow'])
print(f"['brown', 'green', 'yellow'] -> {value4}")

# Example 5: Blue-Grey-Blue. 68 x 10^6 ohms = 68 megaohms
value5 = label(['blue', 'grey', 'blue'])
print(f"['blue', 'grey', 'blue'] -> {value5}")

# Example 6: An invalid color
value_invalid = label(['invalid', 'color', 'red'])
print(f"['invalid', 'color', 'red'] -> {value_invalid}")

# Example 7: Too many colors, as per your request
value_too_many = label(['blue', 'green', 'yellow', 'orange'])
print(f"['blue', 'green', 'yellow', 'orange'] -> {value_too_many}")

# Example 8: Too few colors
value_too_few = label(['red', 'brown'])
print(f"['red', 'brown'] -> {value_too_few}")    